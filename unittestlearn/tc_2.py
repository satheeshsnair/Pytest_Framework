import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\satheeshnair\Desktop\infocampus\SourceCode\AppianJJ\configuration\Drivers\chromedriver.exe")
        self.driver.get("https://www.google.com")
        print("Title of the page is :" + self.driver.title)
        
    def test_search(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\satheeshnair\Desktop\infocampus\SourceCode\AppianJJ\configuration\Drivers\chromedriver.exe")
        self.driver.get("https://jnjtest.appiancloud.com/suite/portal/login.jsp")
        print("Title of the page is :" +self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()