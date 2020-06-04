from selenium.common.exceptions import NoSuchElementException

from Utilities.baseclass import Baseclass


class Orderinfo(Baseclass):

    ordertype = "//div[@class='FieldLayout---input_column']/div/div"
    nextbutton = "//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list']"

    def __init__(self,driver):
        self.driver = driver

    def selectOrdertype(self):
        self.expli_wait(self.ordertype)
        try:
            self.get_list_data(self.ordertype, "test_order", "order")
        except NoSuchElementException:
            print("No element found")

    def clicknext(self):
        self.clickbutton(self.nextbutton)
