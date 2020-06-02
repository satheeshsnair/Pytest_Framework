from Utilities.baseclass import Baseclass


class Orderdetails(Baseclass):

    search_pid = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])[1]"
    next_pid = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])[2]"
    projectid = "//input[@class='TextInput---text TextInput---align_start']"
    checkbox_projectid = "(//div[@class='CheckboxGroup---choice_group CheckboxGroup---no_label CheckboxGroup---align_start'])[2]"

    def __init__(self,driver):
        self.driver = driver

    def project(self):
        self.driver.find_element_by_xpath(self.projectid).send_keys(self.getdata("test_selectOrderType", "projectid"))
        self.driver.find_element_by_xpath(self.search_pid).click()
        self.waits(2)

    def select_project(self):
        self.driver.find_element_by_xpath(self.checkbox_projectid).click()
        self.driver.find_element_by_xpath(self.next_pid).click()
        self.waits(2)