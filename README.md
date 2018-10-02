# README

```sh
pytest -s -v <directory>
python -m pytest
pytest --fixtures
```

## CLI Flags

-c <config-file>
--trace: immediately break on failed tests
--rootdir=ROOTDIR: where to look for tests
-v, q: verbose, quiet
-s: same as --capture=no. Allows print statements through in stdout.
--duration=N: Profile N slowest test durations (pytest --durations=3)
--maxfail=N: Stop test execution at X suites failing
--trace-config: trace considerations of conftest.py files.

## Pytest Fixtures

Fixtures allow test functions to easily receive and work against specific pre-initialized application objects without having to care about import/setup/cleanup details. It’s a prime example of dependency injection where fixture functions take the role of the injector and test functions are the consumers of fixture objects.

Fixtures can have the following scopes:

```py
# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="session")
```

cache | capsys | capsysbinary | capfd | capfdbinary | doctest_namespace | pytestconfig | record_property | record_xml_property | record_xml_attribute | caplog | monkeypatch | recwarn | tmpdir_factory | tmpdir

## Modify the Test Header

```py
def pytest_report_header(config):
    return "project deps: mylib-1.1"
```

## Pytest Function and Decorators

```py
pytest.fail("Failure message!")
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.xfail(strict=True)  # Fails the test suite
@pytest.mark.skipif(sys.version_info < (3, 3), reason="requires python 3.3")

# PARAMETERIZE
from datetime import datetime, timedelta

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected

```

## Exit Codes

Exit code 0: All tests were collected and passed successfully
Exit code 1: Tests were collected and run but some of the tests failed
Exit code 2: Test execution was interrupted by the user
Exit code 3: Internal error happened while executing tests
Exit code 4: pytest command line usage error
Exit code 5: No tests were collected
