import pytest
from pytest import approx
import numpy as np
import sys

# Tests for float equality, accounting for imprecision
0.1 + 0.2 == approx(0.3)
(0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6))
{'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6})
np.array([0.1, 0.2]) + np.array([0.2, 0.4]) == approx(np.array([0.3, 0.6]))
np.array([0.1, 0.2]) + np.array([0.2, 0.1]) == approx(0.3)

# pytest.fail(msg='Arbitrary fail', pytrace=True)
# pytest.fail(msg='Arbitrary fail')


# print(sys.version_info)
@pytest.mark.skipif(sys.version_info < (3, 3), reason="requires python 3.3")
def test_skipif(cmdopt):
  assert 0


@pytest.mark.skip(reason="no way of currently testing this")
def test_skip(cmdopt):
  assert 0


@pytest.mark.xfail(strict=True)  # Fails the test suite
def test_xfail():
  assert 0


