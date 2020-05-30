from typing import List
from vector import dot_product
from statistics.dispersion import delta_mean, standard_deviation


"""Correlation
Measures of statistical dependence between two random variables
"""

def covariance(xs: List[float], ys: List[float]) -> float:
  "Measure of how two variables vary in tandem from their means"
  assert len(xs) == len(ys), "xs and ys must have same number of elements"

  return dot_product(delta_mean(xs), delta_mean(ys)) / (len(xs) - 1)


def correlation(xs: List[float], ys: List[float]) -> float:
  """
  Measure between -1(perfect negative correlation) and 1(perfect postive correlation)
  of linear dependence between x and y. 

  Negative Correlation: values increase/decrease together
  Positive Correlation: increase in values of one variable goes with decrease of the other

  - (x = 1): Perfect Positive Correlation
  - (1 > x > 0.5): Strong Positive Correlation
  - (0.5 > x > 0): Weak Positive Correlation
  - (x = 0): No Correlation
  - (0 > x > -0.5): Weak Negative Correlation
  - (-0.5 > x > -1): Strong Negative Correlation
  - (x = -1): Perfect Negative Correlation
  """
  sd_x = standard_deviation(xs)
  sd_y = standard_deviation(ys)

  if sd_x > 0 and sd_y > 0:
    return covariance(xs, ys) / sd_x / sd_y
  else:
    return 0 # No variation means no correlation

