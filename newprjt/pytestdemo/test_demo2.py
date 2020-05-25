import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_thirdProgram():
    msg = "hello"
    assert msg == "Hai", "Test failed bcoz strings do not match"


def test_fourthPrgm():
    a = 4
    b = 6
    assert a + 2 == b

