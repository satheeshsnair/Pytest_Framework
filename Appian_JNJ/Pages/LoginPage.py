import time
from ResuableLibrary.reusablecodes import reusable
from Utilities.utilities import utils

username = "//*[@id='un']"
password = "//*[@id='pw']"
sign_in = "(//*[@class='btn primary'])[2]"


class loginpage():

    # Constructor-----------------
    def __init__(self, driver):
        self.driver = driver
        self.sharedfunction = reusable(driver)
        self.excelutilities = utils(driver)

    # Methods------------------------------------------------
    # def enter_username(self, testcase, methodname):
    #     data = self.excelutilities.getun(testcase,methodname)
    #     self.driver.find_element_by_xpath(self.username).clear()
    #     self.driver.find_element_by_xpath(self.username).send_keys(data)

    def enter_username(self, uname):
        self.driver.find_element_by_xpath(username).clear()
        self.driver.find_element_by_xpath(username).send_keys(uname)

    def enter_password(self, pword):
        self.driver.find_element_by_xpath(password).send_keys(pword)

    def signin(self):
        self.sharedfunction.clickobj(sign_in)
        time.sleep(3)

    # if __name__ == "__main__":
    #     enter_username("self","satheesh","test")
