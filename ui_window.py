# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 504)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lytLeft = QVBoxLayout()
        self.lytLeft.setObjectName(u"lytLeft")
        self.lytLeft.setContentsMargins(5, 5, 5, 20)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(0)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.cmbFilter = QComboBox(self.groupBox)
        self.cmbFilter.setObjectName(u"cmbFilter")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbFilter)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.cmbSort = QComboBox(self.groupBox)
        self.cmbSort.setObjectName(u"cmbSort")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbSort)

        self.chkDescending = QCheckBox(self.groupBox)
        self.chkDescending.setObjectName(u"chkDescending")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.chkDescending)


        self.lytLeft.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_3 = QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.spnHigh = QDoubleSpinBox(self.groupBox_2)
        self.spnHigh.setObjectName(u"spnHigh")
        self.spnHigh.setDecimals(1)
        self.spnHigh.setMaximum(100.000000000000000)
        self.spnHigh.setValue(100.000000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spnHigh)

        self.spnLow = QDoubleSpinBox(self.groupBox_2)
        self.spnLow.setObjectName(u"spnLow")
        self.spnLow.setDecimals(1)
        self.spnLow.setSingleStep(5.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spnLow)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)


        self.lytLeft.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.lytLeft.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.lytLeft)

        self.lytCenter = QVBoxLayout()
        self.lytCenter.setObjectName(u"lytCenter")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btnLoad = QPushButton(self.centralwidget)
        self.btnLoad.setObjectName(u"btnLoad")

        self.horizontalLayout_3.addWidget(self.btnLoad)

        self.lblFile = QLabel(self.centralwidget)
        self.lblFile.setObjectName(u"lblFile")
        self.lblFile.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lblFile)


        self.lytCenter.addLayout(self.horizontalLayout_3)

        self.tblStudents = QTableWidget(self.centralwidget)
        self.tblStudents.setObjectName(u"tblStudents")
        self.tblStudents.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblStudents.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.lytCenter.addWidget(self.tblStudents)


        self.horizontalLayout.addLayout(self.lytCenter)

        self.lytRight = QVBoxLayout()
        self.lytRight.setSpacing(0)
        self.lytRight.setObjectName(u"lytRight")
        self.lytRight.setContentsMargins(5, 20, 5, 20)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_4 = QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lblTotal = QLabel(self.groupBox_3)
        self.lblTotal.setObjectName(u"lblTotal")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTotal)

        self.lblApproved = QLabel(self.groupBox_3)
        self.lblApproved.setObjectName(u"lblApproved")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblApproved)

        self.lblAverage = QLabel(self.groupBox_3)
        self.lblAverage.setObjectName(u"lblAverage")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblAverage)

        self.lblBest = QLabel(self.groupBox_3)
        self.lblBest.setObjectName(u"lblBest")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblBest)


        self.lytRight.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_5 = QFormLayout(self.groupBox_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.lblHistogram = QLabel(self.groupBox_4)
        self.lblHistogram.setObjectName(u"lblHistogram")
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        self.lblHistogram.setFont(font)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lblHistogram)


        self.lytRight.addWidget(self.groupBox_4)


        self.horizontalLayout.addLayout(self.lytRight)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Analizador de calificaciones", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Filtrar por:", None))
        self.cmbFilter.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ordenar por:", None))
        self.cmbSort.setPlaceholderText("")
        self.chkDescending.setText(QCoreApplication.translate("MainWindow", u"Descendiente", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rango", None))
        self.spnLow.setSpecialValueText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"Cargar Archivo", None))
        self.lblFile.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Resumen", None))
        self.lblTotal.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.lblApproved.setText(QCoreApplication.translate("MainWindow", u"Approved:", None))
        self.lblAverage.setText(QCoreApplication.translate("MainWindow", u"Average:", None))
        self.lblBest.setText(QCoreApplication.translate("MainWindow", u"Best:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Histograma", None))
        self.lblHistogram.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
    # retranslateUi

