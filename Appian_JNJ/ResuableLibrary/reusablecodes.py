import time


class reusable():

    def __init__(self,driver):
        self.driver = driver

    def clickobj(self,locator):
        time.sleep(3)
        self.driver.find_element_by_xpath(locator).click()
