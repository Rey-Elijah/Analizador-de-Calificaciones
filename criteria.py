import operator as op
from collections.abc import Callable

import analysis
from model import Student


def in_group(group:str) -> Callable[[Student], bool]:
    """ex:'in_group("7A")' returns a predicate that answers if a student is from group 7A"""
    return lambda student: student.group == group

def average_at_least(minimum: float) -> Callable[[Student], bool]:
    """ex: 'average_at_least(80)' returns a predicate that answers if a student average is at least 80"""
    return lambda student: analysis.average(student) >= minimum

def both(predicate1:Callable, predicate2:Callable) -> Callable[[Student], bool]:
    """high order function that returns a new predicate that is True when predicate1/2 are both True for the same input"""
    return lambda x: predicate1(x) and predicate2(x)

def negate(predicate:Callable) -> Callable:
    """negates the result of the passed predicated"""
    return lambda x : not predicate(x)

def query(students, predicate, key, descending=False) -> tuple[Student, ...]:
    """Filters and orders the students as requested"""
    return tuple(sorted(filter(predicate, students), key=key, reverse=descending))

# list of filters to show in the combo 'filter'
FILTERS:dict[str, Callable] = {
    "Todos": lambda s: True,
    "Aprobados": analysis.is_approved,
    "Reprobados": negate(analysis.is_approved),
    "Grupo 7A": in_group("7A"),
    "Grupo 7B": in_group("7B"),
}

SORT_KEYS = {
    "Nombre": op.attrgetter("name"), # returns a callable that search the named attribute name
    "Promedio": analysis.average,
    "Matricula": op.attrgetter("controlN"),
    "Grupo": op.attrgetter("group"),
}

if __name__ == "__main__":
    from reading import read_students
    ana:Student = Student("23940499", "Ana", "7A", (100, 60, 100, 100))
    students = tuple(read_students("datos/calificaciones.csv"))
    # first test
    print(len(query(students, in_group("7A"), SORT_KEYS["Nombre"])))
    # second test
    approved_7A = both(in_group("7A"), analysis.is_approved)
    print(len(tuple(filter(approved_7A, students))))
    # third test
    atleast_80_in_7B = both(average_at_least(80), in_group("7B"))
    print(query(students, atleast_80_in_7B, SORT_KEYS["Promedio"], descending=True))