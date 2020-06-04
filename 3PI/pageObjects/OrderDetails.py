from Utilities.baseclass import Baseclass


class Orderdetails(Baseclass):

    search_pid = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])[1]"
    next_pid = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])[2]"
    projectid = "(//input[@class='TextInput---text TextInput---align_start'])[1]"
    checkbox_projectid = "(//div[@class='CheckboxGroup---choice_group CheckboxGroup---no_label CheckboxGroup---align_start'])[2]"

    def __init__(self,driver):
        self.driver = driver

    def project(self):
        self.expli_wait(self.projectid)
        self.driver.find_element_by_xpath(self.projectid).send_keys(self.getdata("test_selectOrderType", "projectid"))
        self.expli_wait(self.search_pid)
        self.driver.find_element_by_xpath(self.search_pid).click()

    def select_project(self):
        self.expli_wait(self.checkbox_projectid)
        self.driver.find_element_by_xpath(self.checkbox_projectid).click()
        self.expli_wait(self.next_pid)
        self.driver.find_element_by_xpath(self.next_pid).click()