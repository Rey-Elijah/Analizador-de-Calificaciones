from typing import NamedTuple


class Student(NamedTuple):
    controlN:str
    name:str
    group:str
    grades:tuple[int, ...] # zero or more int's values

def row_to_student(row:list[str]) -> Student:
    """
    receives a row that is a list of strings containing the student
    data and returns a new Student object by using that data
    """
    controlN, name, group, *grades = row #desempaquetado
    return Student(controlN, name, group, tuple(map(int, grades)))

if __name__ == "__main__":
    fila = ['22130100', 'Ana Lopez Diaz', '7A', '64', '72', '80', '61']
    print(row_to_student(fila))