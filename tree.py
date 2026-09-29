from model import Student
from analysis import average
from functools import reduce
from collections.abc import Iterator

# Recursive type definition
type Tree = tuple[Student, "Tree", "Tree"] | None

def insert(tree: Tree, student: Student = None) -> Tree: # type: ignore
    """**insert()**
    fnc that adds a student (second argument) to the given three (first argument)
    Args:
        tree:
            tree/subtree object of type `tuple`
        student:
            student object of type `Student`
    Returns:
        a new tree node
    
        """
    if tree is None:
        return (student, None, None) # new root/node
    # unpacking the values
    node, left, right = tree
    # organize by grades
    if average(student) < average(node):
        return (node, insert(left, student), right) # new left node
    else:
        return (node, left, insert(right, student)) # new right node

def build_tree(students:tuple[Student, ...]) -> Tree:
    """**build_tree()**
    Args:
        students:
            `tuple` containing objects of type `Student`
    Returns:
        A `tuple` representing the `tree` created
    """
    # if None or empty
    if students is None or not students:
        return ()
    return tuple(reduce(lambda acc, s: insert(acc, s), students, None))

def in_order(tree: Tree) -> Iterator[Student]:
    """**in_order():**
    fnc that creates a generator containing the students inside
    the given tree sorted by grades in ascendant order
    Args:
        tree:
            `tuple` representing a tree of students (Student, Tree, Tree)
        Returns:
            a `Iterator`"""
    if tree is None:
        return
    node, left, right = tree
    yield from in_order(left) # exausted left
    yield node  # node
    yield from in_order(right) # exausted right

def in_range(tree: Tree, low:float, high:float) -> Iterator[Student]:
    """**in_range():**
    fnc that creates a generator containing the students inside
    the given tree sorted by grades and filtered between a range (low, high)
    Args:
        tree:
            `tuple` representing a tree of students (Student, Tree, Tree)
        Returns:
            a `Iterator`"""
    if tree is None:
        return
    node, left, right = tree

    if average(node) < low:
        # node is too small -> left subtree is even smaller -> skip left
        yield from in_range(right, low, high)

    elif average(node) >= high:
        # node is too big -> right subtree is even bigger -> skip right
        yield from in_range(left, low, high)

    else:
        # low <= node.grades < hight -> this node is a result
        yield from in_range(left, low, high)
        yield node
        yield from in_range(right, low, high)

def height(tree: Tree) -> int:
    if tree is None:
        return 0 # empty -> height 0
    _node, left, right = tree
    return 1 + max(height(left), height(right)) # this node + taller child

if __name__ == "__main__":
    from reading import read_students
    students:tuple = tuple(read_students("datos/calificaciones.csv"))
    ana:Student = students[0]
    luis:Student = students[1]

    tree = build_tree(students)
    # the first from the three
    #print(tree[0].name)
    # all averages in ascendant order (40 in total)
    #print([round(average(s), 2) for s in in_order(tree)])
    # how many students in the range of 80 and 90 are
    #print(len(tuple(in_range(tree, 80, 90))))
    """t1 = build_tree(students[:5])
    t2 = insert(t1, students[5])
    print(t1[1] is t2[1]) # False: 6th student fell in left branch and its different
    print(t1[2] is t2[2]) # True: right branch is shared and its the same"""
    hey = tuple()
    t = build_tree(hey)