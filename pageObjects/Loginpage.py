from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utilities.baseclass import Baseclass

class LoginPage(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    # ********************Locators*****************#
    username = (By.XPATH, "//*[@id='un']")
    password = (By.XPATH, "//*[@id='pw']")
    signin_button = (By.XPATH, "(//*[@class='btn primary'])[2]")

    # ********************Functions*****************#

    def getusername(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*LoginPage.username).clear()
            self.driver.find_element(*LoginPage.username).send_keys(self.getdata("test_login","Username"))
            log.info("Username entered")
        except Exception as error:
            log.error(error)

    def getpassword(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*LoginPage.password).clear()
            self.driver.find_element(*LoginPage.password).send_keys(self.getdata("test_login", "Password"))
            log.info("Password entered")
        except Exception as error:
            log.error(error)

    def signinbutton(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*LoginPage.signin_button).click()
            log.info("Clicked on Sign in button")
        except Exception as error:
            log.error(error)