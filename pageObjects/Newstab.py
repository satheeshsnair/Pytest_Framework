from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utilities.baseclass import Baseclass


class NewsTab(Baseclass):

    def __init__(self,driver):
        self.driver = driver

    actionstab = (By.XPATH,"//div[contains(text(),'Actions')]")
    reportstab = (By.XPATH,"//div[contains(text(),'Reports')]")
    recordstab = (By.XPATH,"//div[contains(text(),'Records')]")
    taskstab   = (By.XPATH,"//div[contains(text(),'Tasks')]")

    def clickonActiontab(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*NewsTab.actionstab).click()
            log.info("Clicked on Action Tab")
        except Exception as error:
            log.error(error)

    def clickonRecordstab(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*NewsTab.recordstab).click()
            log.info("Clicked on Records Tab")
        except Exception as error:
            log.error(error)