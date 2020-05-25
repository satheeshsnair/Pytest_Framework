import pytest


@pytest.fixture(scope="class")
def setup():
    print("Executed first")
    yield
    print("executed last")
