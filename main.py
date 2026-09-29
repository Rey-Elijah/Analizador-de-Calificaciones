"""
main.py
Imperative shell: the only part of the app with side effects (reading files, painting widgets).
All the logic lives in pure functions (analysis, criteria, tree, view).
"""
import math
import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, 
    QFileDialog, 
    QHeaderView, 
    QMainWindow,
    QMessageBox, 
    QTableWidgetItem
)

from criteria import FILTERS, SORT_KEYS, query
from reading import read_students
from tree import build_tree, in_range
from ui_window import Ui_MainWindow
from view import HEADERS, histogram_text, student_row, summary_texts

# csv loaded when the app starts (next to this file, not where the terminal is)
DEFAULT_CSV = Path(__file__).parent / "datos" / "calificaciones.csv"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("tole.ico"))

        # the ONLY state of the app: the loaded data.
        # it is never modified, only replaced when another file is loaded
        self.students: tuple = ()
        self.tree = None

        self.setup_widgets()
        self.connect_signals()

        if DEFAULT_CSV.exists():
            self.load_path(str(DEFAULT_CSV))

    def setup_widgets(self):
        """**setup_widgets():**
        fills the combos and the table headers from the dictionaries and HEADERS
        (single source of truth: adding a filter to FILTERS adds it here too)"""
        self.ui.cmbFilter.addItems(list(FILTERS))
        self.ui.cmbSort.addItems(list(SORT_KEYS))

        table = self.ui.tblStudents
        table.setColumnCount(len(HEADERS))
        table.setHorizontalHeaderLabels(HEADERS)
        table.verticalHeader().setVisible(False)  # hides the row numbers
        table.setWordWrap(False)  # one line per student
        # columns fit their content, the name column takes the free space
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        self.ui.lblBest.setWordWrap(True)  # long names go to a second line
        self.ui.lblFile.setText("Sin archivo")

    def connect_signals(self):
        """**connect_signals():**
        every control recalculates everything when it changes.
        connect() receives a function as argument: higher order function"""
        self.ui.btnLoad.clicked.connect(self.load_file)
        for signal in (
            self.ui.cmbFilter.currentTextChanged,
            self.ui.cmbSort.currentTextChanged,
            self.ui.chkDescending.toggled,
            self.ui.spnLow.valueChanged,
            self.ui.spnHigh.valueChanged,
        ):
            signal.connect(self.refresh)

    def load_file(self):
        """**load_file():**
        asks the user for a csv file and loads it"""
        path, _ = QFileDialog.getOpenFileName(self, "Abrir CSV", str(DEFAULT_CSV.parent), "CSV (*.csv)")
        if path:  # empty string means the user canceled
            self.load_path(path)

    def load_path(self, path: str):
        """**load_path():**
        the boundary with the outside world: the file is read ONCE,
        then the data is stored as an immutable tuple and a tree
        Args:
            path: path of the csv file"""
        try:
            students = tuple(read_students(path))
        except (ValueError, IndexError, OSError) as e:
            QMessageBox.warning(self, "Error", f"No se pudo leer el archivo:\n{e}")
            return

        # replace the whole state at once
        self.students = students
        self.tree = build_tree(students) if students else None
        self.ui.lblFile.setText(Path(path).name)
        self.refresh()

    def refresh(self, *_):
        """**refresh():**
        the full pipeline: tree + range -> filter -> sort -> render.
        *_ ignores the value that each signal sends"""
        low = self.ui.spnLow.value()
        # in_range excludes 'high'; nextafter gives the next float after it,
        # so a student with exactly 100.0 is included when Max = 100
        high = math.nextafter(self.ui.spnHigh.value(), math.inf)

        predicate = FILTERS[self.ui.cmbFilter.currentText()]
        key = SORT_KEYS[self.ui.cmbSort.currentText()]
        descending = self.ui.chkDescending.isChecked()

        in_interval = in_range(self.tree, low, high) if self.tree else ()
        result = query(in_interval, predicate, key, descending)
        self.render(result)

    def render(self, students: tuple):
        """**render():**
        the ONLY method that touches widgets. It does not calculate anything,
        it just paints the data that view.py already prepared
        Args:
            students: `tuple` of students to show"""
        rows = tuple(map(student_row, students))
        table = self.ui.tblStudents
        table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(value))

        # pairs each label with its text: (lblTotal, "Total: 40"), ...
        labels = (self.ui.lblTotal, self.ui.lblApproved, self.ui.lblAverage, self.ui.lblBest)
        for label, text in zip(labels, summary_texts(students)):
            label.setText(text)

        self.ui.lblHistogram.setText(histogram_text(students))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())