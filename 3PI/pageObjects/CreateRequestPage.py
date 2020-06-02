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

    ordertype = "//div[@class='FieldLayout---input_column']/div/div"
    nextbutton = "//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list']"
    search_pid = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])[1]"
    next_pid = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])[2]"
    projectbased = "//label[contains(text(),'Project Based')]"
    projectid = "//input[@class='TextInput---text TextInput---align_start']"
    checkbox_projectid = "(//div[@class='CheckboxGroup---choice_group CheckboxGroup---no_label CheckboxGroup---align_start'])[2]"
    country = "(//div[@class='FieldLayout---input_column']/div/div)[1]"
    supplier = "(//div[@class='FieldLayout---input_column']/div/div)[3]"
    capital = "(//*[@class='TextInput---text TextInput---align_start'])[3]"
    expense = "(//*[@class='TextInput---text TextInput---align_start'])[4]"
    quote = "(//*[@class='TextInput---text TextInput---align_start'])[5]"
    upload = "//*[@class='FileUploadWidget---ui-inaccessible']"
    docname = ("//*[@class='FileUploadWidget---upload_item']/div[2]/p/strong")

    def __init__(self,driver):
        self.driver = driver

    def selectOrdertype(self):
        self.waits(10)
        try:
            self.get_list_data(self.ordertype, "test_order", "order")
        except NoSuchElementException:
            print("No element found")

    def clicknext(self):
        self.clickbutton(self.nextbutton)

    def project(self):
        self.driver.find_element_by_xpath(self.projectid).send_keys(self.getdata("test_selectOrderType","projectid"))
        self.driver.find_element_by_xpath(self.search_pid).click()
        self.waits(2)
        self.driver.find_element_by_xpath(self.checkbox_projectid).click()
        self.driver.find_element_by_xpath(self.next_pid).click()
        self.waits(2)

    def prjinfo(self):
        self.get_list_data(self.country,"test_projectinfo","country")
        self.driver.find_element_by_xpath(self.capital).send_keys(self.getdata("test_projectinfo","Capital Amount"))
        self.driver.find_element_by_xpath(self.expense).send_keys(self.getdata("test_projectinfo", "Expense Amount"))
        self.driver.find_element_by_xpath(self.quote).send_keys(self.getdata("test_projectinfo", "Quote Number"))
        self.waits(2)
        self.get_list_data(self.supplier, "test_projectinfo", "Supplier")
        self.uploadfile(self.upload, self.getdata("test_projectinfo", "path"))