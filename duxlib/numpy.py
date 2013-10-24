from __future__ import absolute_import

import numpy as np
from scipy.stats import scoreatpercentile


def inner(arr, p, sorted=False):
  """Get mask for points in `arr` that form the inner `p` percentage of points when sorted"""
  arr = np.asarray(arr)
  sorted = np.argsort(arr)
  p = 1-p
  p_low, p_high = 100 * p/2.0, 100 * (1-p/2.0)
  lower, upper = scoreatpercentile(sorted, [p_low, p_high])
  return (arr >= lower) & (arr <= upper)
