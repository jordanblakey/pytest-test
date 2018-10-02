# content of conftest.py
import pytest
import smtplib


# Modify the Test header
def pytest_report_header(config):
    return "project deps: mylib-1.1"


# Parse command line options to pytest
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


# Create objects for use by tests in a specific scope/context
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="session")
@pytest.fixture(scope="module")
def smtp_connection():
  smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
  # FIXTURE TEARDOWN
  yield smtp_connection
  print("teardown smtp")  # Executes when the last test in module (scope) finishes
  smtp_connection.close()
