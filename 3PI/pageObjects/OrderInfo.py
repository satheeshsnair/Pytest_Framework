from selenium.common.exceptions import NoSuchElementException

from utilities.baseclass import Baseclass


class Orderinfo(Baseclass):

    ordertype = "//div[@class='FieldLayout---input_column']/div/div"
    nextbutton = "//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list']"

    def __init__(self,driver):
        self.driver = driver

    def selectOrdertype(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.ordertype)
            self.get_list_data(self.ordertype, "test_order", "order")
            log.info("Order tye selected")
        except Exception as error:
            log.error(error)


    def clicknext(self):
        log = self.getLogger()
        try:
            self.clickbutton(self.nextbutton)
            log.info("Next button clicked")
        except Exception as error:
            log.error(error)
