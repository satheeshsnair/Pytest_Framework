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
    def login(self):
        self.driver.find_element(*LoginPage.username).send_keys("satheeshnair@kpmg.com")
        self.driver.find_element(*LoginPage.password).send_keys("Welcome26")
        self.driver.find_element(*LoginPage.signin_button).click()

    def getusername(self):
        self.driver.find_element(*LoginPage.username).send_keys(self.getdata("test_login","Username"))

    def getpassword(self):
        self.driver.find_element(*LoginPage.password).send_keys(self.getdata("test_login", "Password"))

    def signinbutton(self):
        self.driver.find_element(*LoginPage.signin_button).click()