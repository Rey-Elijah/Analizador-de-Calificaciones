import operator as op

from functools import reduce
from model import Student

def average(student: Student) -> float:
    """**average()**:
    fnc that returns the average of all the grades of the given student
    Args:
        student:object of class `Student`
    Returns:
        a `float` representing the average"""
    if student is None:
        return 0.0
    # average = X1 + X2 + ... Xn / n
    return sum(student.grades) / len(student.grades)
    #return op.truediv((reduce(lambda x, y: x + y, student.grades)), len(student.grades))

def is_approved(student: Student) -> bool:
    """**is_approved():**
    predicate that indicates if the given student passed the semester
    Args:
        student:object of class `Student`
    Returns:
        a `bool`"""
    return all(grade >= 70.0 for grade in student.grades)

def failed_units(student: Student) -> tuple[int, ...]:
    """**failed_units():
    Args:
        student:object of class `Student`
    Returns:
        a `tuple` with more tuples inside each one containing pairs of `int` indicating the unit failed
        and the grade respectively ('2, 45' for ex.)"""
    #return tuple((i, grade) for i, grade in enumerate(student.grades, start=1) if grade < 70.0)
    return tuple(unit for unit, grade, in enumerate(student.grades, start=1) if grade < 70)

def approved(students: tuple[Student, ...]) -> tuple[Student, ...]:
    """**approved():**
    Args:
        students:`tuple` containing objects of type `Student`
    Returns:
        a `tuple` of the approved students from the tuple given as argument"""
    return tuple(filter(is_approved, students))

def best_student(students: tuple[Student, ...]) -> Student | None:
    """**best_student():**
    Args:
            students:`tuple` containing objects of type `Student`
    Returns:
        the student with the best average inside the tuple given as argument
    """
    if not students:return None
    #return reduce(lambda a, b: a if average(a) > average(b) else b, students)
    return max(students, key=average)

def group_average(students: tuple[Student, ...]) -> float:
    """**group_average()**
    Args:
        students:`tuple` containing objects of type `Student`
    Returns:
        the general average between the passed tuple of students
    """
    if not students:return 0.0 
    # Avg1 + Avg2 + ... AvgN / N
    total:float = reduce(lambda a, b: a + b, map(average, students))
    return op.truediv(total, len(students))

def make_ranges() -> tuple[range, ...]:
    """**make_ranges()**
    Returns:
        a tuple of ranges between; (0,60), (60,70), (70,80), (80,90) and (90,100)
    """
    return (
        range(0, 60),
        * (range(i, i + 10) for i in range(60, 90, 10)),
        range(90, 101)
    )

def range_label(r: range) -> str:
    """**range_label()**
    Args:
        r: The input value of type `range`.
    Returns:
        A formatted `string` indicating the `initial` and `final` value inside
        the **passed range**
    """
    return f"{r.start}-{r[-1]}"

def histogram(students: tuple[Student, ...]) -> tuple[tuple[str, int], ...]:
    """**histogram**.
        Args:
            students: The input value of type tuple[Student, ...]
        Returns:
            A `tuple` with tuples inside, each one having pairs of string and int, the first one indicating `a range
            of numbers` (0-59, 60-69 for ex.) and the second one indicating the `amount of student averages`
            inside those ranges respectively
    """
    averages:tuple = tuple(map(average, students))
    return tuple(
        (range_label(r), sum(1 for avg in averages if r.start <= avg < r.stop))
        #^ label          ^ count
        for r in make_ranges()
        # iterates over each range
    )

if __name__ == "__main__":
    from reading import read_students

    #print(make_ranges())
    """rango = range(60, 70)
    print(range_label(rango))"""

    
    students:tuple = tuple(read_students("datos/calificaciones.csv"))
    #print(histogram(students))
    print(make_ranges())
