import unittest
import html
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("This is login test")

    @classmethod
    def tearDownClass(self):
        print("logout")

    def test_search1(self):
        print("Test1")

    def test_search2(self):
        print("Test2")

    def test_search3(self):
        print("Test3")

    def test_search4(self):
        print("Test4")

if __name__ == "__main__":
    unittest.main()