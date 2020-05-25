# Any pytest file should start with test_
import pytest

@pytest.mark.usefixtures("setup")
class Testexample:
    @pytest.mark.smoke
    def test_firstProgram(self):
        print("hello satheesh")


    def test_secdPrgm(self):
        print("second test")


