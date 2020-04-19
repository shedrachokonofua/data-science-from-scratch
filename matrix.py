"""
Rudimentary matrix & matrix operations implementation
"""
from typing import List, Tuple, Callable

"""Matrix
A two-dimensional collection of numbers
"""
Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int, int]:
  num_rows = len(A)
  num_cols = len(A[0]) if A else 0
  return (num_rows, num_cols)

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, i: int) -> List[float]:
  return A[i]

assert get_row([[1, 2, 3], [4, 5, 6]], 0) == [1, 2, 3]


def get_column(A: Matrix, i: int) -> List[float]:
  return [row[i] for row in A]

assert get_column([[1, 2, 3], [4, 5, 6]], 0) == [1, 4]


def make_matrix(
  num_rows: int,
  num_cols: int,
  fn: Callable[[int, int], float]
) -> Matrix:
  return [[fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(size: int) -> Matrix:
  return make_matrix(size, size, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1]
]