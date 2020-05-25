import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.baseclass import Baseclass


class CreateReq():

    def __init__(self,driver):
        self.driver = driver

    # ordertype = (By.XPATH,"//*[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder']")
    ordertype = ("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder']")
    # ordertype = (By.XPATH, "(//*[@class ='RadioSelect---choice_label'])[1]")

    def selectOrdertype(self):
        print(self.ordertype)
        time.sleep(40)
        self.driver.find_element_by_xpath(self.ordertype).click()
        # elem = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "ordertype")))
        # elem.click()
        # action = ActionChains(self.driver);
        # print("actions class")
        # Ordersel = self.driver.find_element_by_xpath(self.ordertype)
        # action.move_to_element(Ordersel).perform()
        # print("perform done")
        # Ordersel.click()
