# Test discovery: test_*.py

def func(x):
  return x + 1

# This will pass
def test_answer():
  assert func(4) == 5

# This will fail
# def test_answer():
#   assert func(3) == 5
