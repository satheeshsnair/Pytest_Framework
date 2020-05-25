import allure
import pytest_html
import pytest

@pytest.yield_fixture()
def setup():
    print("Once b4 every method")
    yield
    print("after every method")

def test_method1(setup):
    print("Pytest demo")

def test_m2():
    print("demo 2")