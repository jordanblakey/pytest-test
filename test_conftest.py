import pytest

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 1  # to see what was printed


# def checkconfig(x):
#     __tracebackhide__ = True
#     if not hasattr(x, "config"):
#         pytest.fail("not configured: %s" % (x,))


# def test_something():
#     checkconfig(42)


# def test_arbitrary_fail():
#   pytest.fail("Arbitrary test failure!")
