import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.baseclass import Baseclass
driver = None


class CreateReq(Baseclass):

    # ordertype = "//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder']"
    ordertype = "//div[@class='FieldLayout---input_column']/div/div"
    nextbutton = "//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list']"

    def __init__(self,driver):
        self.driver = driver

    def selectOrdertype(self):
        print(self.ordertype)
        time.sleep(10)
        try:
            self.driver.find_element_by_xpath(self.ordertype).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(self.ordertype).send_keys("Server")
            time.sleep(3)
            self.driver.find_element_by_xpath(self.ordertype).click()
        except NoSuchElementException:
            print("No element found")

    def clicknext(self):
        self.clickbutton(self.nextbutton)
