from typing import List
from collections import Counter
from fixtures import quantile_test_data


"""Central Tendency
Different measures of the "centrality" of our data.
"""

def mean(xs: List[float]) -> float:
  return sum(xs) / len(xs)

assert mean([4, 5, 6]) == 5


def _median_odd(xs: List[float]) -> float:
  return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
  high_midpoint = len(xs) // 2
  low_midpoint = high_midpoint - 1
  sorted_xs = sorted(xs)
  return (sorted_xs[high_midpoint] + sorted_xs[low_midpoint]) / 2


def median(xs: List[float]) -> float:
  is_even_size_set = len(xs) % 2 == 0
  fn = _median_even if is_even_size_set else _median_odd
  return fn(xs)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 2, 9, 6]) == 4


def quantile(xs: List[float], p: float) -> float:
  """Returns the p-th percentile value in x"""
  p_index = int(p * len(xs))
  return sorted(xs)[p_index]

assert quantile(quantile_test_data, 0.10) == 2
assert quantile(quantile_test_data, 0.25) == 3
assert quantile(quantile_test_data, 0.75) == 8
assert quantile(quantile_test_data, 0.90) == 10


def mode(xs: List[float]) -> List[float]:
  """Returns the most common value(s) in x"""
  counts = Counter(xs)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.items() if count == max_count]

assert mode([1, 1, 1, 2, 2, 3]) == [1]
assert mode([1, 1, 2, 2, 3]) == [1, 2]

