from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import loginpage
import pytest
from Utilities.baseclass import BaseClass


class E2eTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\satheeshnair\Desktop\infocampus\SourceCode\AppianJJ\configuration\Drivers\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login(self):
        # driver = self.driver
        # driver.get('https://jnjtest.appiancloud.com/suite/portal/login.jsp')
        login = loginpage(self.driver)
        # home = homepage(driver)
        # action = actionspage(driver)
        login.enter_username("vendor3_ibm")
        login.enter_password('Welcome26')
        login.signin()

    # def test_clickActionTab(self):
    #     home.clickActionTab()

    # def test_selectorderreq(self):
    #     self.action.select_sumitorder()
