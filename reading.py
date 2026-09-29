import csv
from collections.abc import Iterator

from model import Student, row_to_student


def read_students(path:str) -> Iterator[Student]:
    """
    Reads a csv file efficiently and returns a Students generator
    """
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        # row 0 are the headers so with this fnc the reader advance to the next row where the students rows starts
        next(reader)    
        # yields the Student reading
        yield from map(row_to_student, reader)

if __name__ == "__main__":
    students = read_students("datos/calificaciones.csv")
    print(students)             # prints the memory direction of the generator
    print(next(students))       # first student
    print(next(students))       # second
    print(len(list(students)))  # a generator runs out so this returns 38 instead of 40 because the 2 next() at the start consumed 2 Students from the generator