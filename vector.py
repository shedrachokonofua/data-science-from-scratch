"""
Rudimentary vector & vector operations implementation
"""

from typing import List
import math

Vector = List[float]

def add(v: Vectordot, w: Vector) -> Vector:
  assert len(v) == len(w), "vectors must have an equal number of components"

  return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
  assert len(v) == len(w), "vectors must have an equal number of components"

  return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
  assert vectors, "no vectors provided"

  # check that vectors all have the same number of components
  num_components = len(vectors[0])
  assert all(len(v) == num_components for v in vectors), "inconsistent vector sizes"

  return [sum(v[i] for v in vectors) for i in range(num_components)]

assert vector_sum([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == [15, 20]


def scalar_multiply(c: float, vector: Vector) -> Vector:
  return [c * v_i for v_i in vector]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4 ,6]


def vector_mean(vectors: List[Vector]) -> Vector:
  n = len(vectors)
  return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot_product(v: Vector, w: Vector) -> float:
  """Dot Product
  Given 2 vectors, v and w, the dot product of v and w is the length of the
  projection of x onto y. Simply, it is the measure of how much v goes in the
  direction of w.
  """
  assert len(v) == len(w), "vectors must have an equal number of components"

  return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
  return dot_product(v, v)

assert sum_of_squares([1, 3]) == 10


def magnitude(v: Vector) -> float:
  """Magnitude
  The scalar length of a vector
  """
  return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5