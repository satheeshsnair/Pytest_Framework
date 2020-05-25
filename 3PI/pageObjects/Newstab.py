from selenium.webdriver.common.by import By


class NewsTab:

    def __init__(self,driver):
        self.driver = driver

    actionstab = (By.XPATH,"//div[contains(text(),'Actions')]")
    reportstab = (By.XPATH,"//div[contains(text(),'Reports')]")
    recordstab = (By.XPATH,"//div[contains(text(),'Records')]")
    taskstab   = (By.XPATH,"//div[contains(text(),'Tasks')]")

    def clickonActiontab(self):
        self.driver.find_element(*NewsTab.actionstab).click()