from Utilities.baseclass import Baseclass
username = "//*[@id='un']"
password = "//*[@id='pw']"
sign_in = "(//*[@class='btn primary'])[2]"


class TestE2e(Baseclass):

    def test_login(self):
        self.driver.find_element_by_xpath(username).clear()
        self.driver.find_element_by_xpath(username).send_keys("vendor3_ibm")
        self.driver.find_element_by_xpath(password).send_keys("Welcome26")