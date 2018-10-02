import pytest


def f():
  raise SystemExit(1)


def test_mytest():
  # Tests that a specific Exception is raised
  with pytest.raises(SystemExit):
    f()
