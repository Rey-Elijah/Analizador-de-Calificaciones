"""
view.py
Pure functions that turn students into ready-to-show texts.
No Qt here: everything can be tested with a simple print().
"""
import analysis
from model import Student

# table columns; student_row() must return the values in this same order
HEADERS: tuple[str, ...] = ("Matricula", "Nombre", "Grupo", "U1", "U2", "U3", "U4",
                            "Promedio", "Estado", "Reprobadas")


def student_row(student: Student) -> tuple[str, ...]:
    """**student_row():**
    Args:
        student: object of class `Student`
    Returns:
        a `tuple` of strings, one per column of HEADERS
    """
    status = "Aprobado" if analysis.is_approved(student) else "Reprobado"
    # (1, 4) -> "1, 4" ; empty tuple -> "-"
    failed = ", ".join(map(str, analysis.failed_units(student))) or "-"
    return (
        student.controlN,
        student.name,
        student.group,
        *map(str, student.grades),  # unpacks the 4 grades as strings
        f"{analysis.average(student):.2f}",
        status,
        failed,
    )


def summary_texts(students: tuple[Student, ...]) -> tuple[str, str, str, str]:
    """**summary_texts():**
    Args:
        students: `tuple` containing objects of type `Student`
    Returns:
        (total, approved, average, best) as texts for the summary labels
    """
    best = analysis.best_student(students)  # can be None if there are no students
    best_text = f"Mejor: {best.name} ({analysis.average(best):.2f})" if best else "Mejor: -"
    return (
        f"Total: {len(students)}",
        f"Aprobados: {len(analysis.approved(students))}",
        f"Promedio: {analysis.group_average(students):.2f}",
        best_text,
    )


def histogram_bar(label: str, count: int, scale: float) -> str:
    """**histogram_bar():**
    Args:
        label: range label, ex. "60-69"
        count: how many students are in that range
        scale: how many characters represent one student
    Returns:
        one text line, ex. " 60-69 ██████████ 10"
    """
    return f"{label:>6} {'█' * round(count * scale)} {count}"


def histogram_text(students: tuple[Student, ...], max_width: int = 15) -> str:
    """**histogram_text():**
    Args:
        students: `tuple` containing objects of type `Student`
        max_width: length of the longest bar, so it fits in the panel
    Returns:
        the whole histogram as a multi-line `str`
    """
    data = analysis.histogram(students)
    biggest = max((count for _, count in data), default=0)
    scale = max_width / biggest if biggest else 0  # avoids division by zero
    return "\n".join(histogram_bar(label, count, scale) for label, count in data)


if __name__ == "__main__":
    from reading import read_students

    students = tuple(read_students("datos/calificaciones.csv"))
    print(student_row(students[0]))
    print(summary_texts(students))
    print(histogram_text(students))
    print(summary_texts(()))  # empty case must not crash
