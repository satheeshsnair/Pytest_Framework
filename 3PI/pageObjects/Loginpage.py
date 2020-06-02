from selenium.webdriver.common.by import By

from Utilities.baseclass import Baseclass


class LoginPage(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    # ********************Locators*****************#
    username = (By.XPATH, "//*[@id='un']")
    password = (By.XPATH, "//*[@id='pw']")
    signin_button = (By.XPATH, "(//*[@class='btn primary'])[2]")

    # ********************Functions*****************#

    def getusername(self):
        self.driver.find_element(*LoginPage.username).send_keys(self.getdata("test_login","Username"))
        self.waits(2)

    def getpassword(self):
        self.driver.find_element(*LoginPage.password).clear()
        self.driver.find_element(*LoginPage.password).send_keys(self.getdata("test_login", "Password"))

    def signinbutton(self):
        self.driver.find_element(*LoginPage.signin_button).click()