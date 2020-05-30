from typing import List
import math
from vector import sum_of_squares
from statistics.central_tendency import mean, quantile
from fixtures import quantile_test_data


"""Dispersion
Different measures of how spread out our data is.
"""

def data_range(xs: List[float]) -> float:
  return max(xs) - min(xs)

assert data_range([1, 2, 3, 4, 5]) == 4


def delta_mean(xs: List[float]) -> List[float]:
  x_mean = mean(xs)
  return [x - x_mean for x in xs]


def variance(xs: List[float]) -> float:
  "Average squared deviation from the mean"
  assert len(xs) >= 2, "variance requires at least two elements"

  n = len(xs)
  deviations = delta_mean(xs)
  return sum_of_squares(deviations) / (n - 1)

assert variance([1, 2, 3, 4, 5]) == 2.5


def standard_deviation(xs: List[float]) -> float:
  "Square root of variance"
  return math.sqrt(variance(xs))

assert standard_deviation([1, 2, 3, 4, 5]) == math.sqrt(2.5)


def interquartile_range(xs: List[float]) -> float:
  "Returns the difference between the 75%-ile and the 25%-ile"
  return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquartile_range(quantile_test_data) == 5
