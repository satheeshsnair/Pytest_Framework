from selenium.webdriver.common.by import By

from utilities.baseclass import Baseclass


class ActionsTab(Baseclass):

    def __init__(self,driver):
        self.driver = driver

    submitorderrequest = (By.XPATH, "//a[contains(text(),'3PI Submit Order Request')]")

    def clickon3PISubmitOrderRequest(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*ActionsTab.submitorderrequest).click()
            log.info("Clicked on 3PI Submit Order Request")
        except Exception as error:
            log.error(error)