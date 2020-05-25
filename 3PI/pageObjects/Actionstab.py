from selenium.webdriver.common.by import By


class ActionsTab:

    def __init__(self,driver):
        self.driver = driver

    submitorderrequest = (By.XPATH, "//a[contains(text(),'3PI Submit Order Request')]")

    def clickon3PISubmitOrderRequest(self):
        self.driver.find_element(*ActionsTab.submitorderrequest).click()