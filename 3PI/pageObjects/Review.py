from utilities.baseclass import Baseclass


class Review(Baseclass):

    def __init__(self,driver):
        self.driver = driver

    # order_title = "(//*[@class='FieldLayout---input_column']/p/text())[1]"
    order_title = "(//*[@class='FieldLayout---input_column']/p)[1]"
    nextbutton = "//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list']"

    def get_Order_title(self):
        log = self.getLogger()
        try:
            self.waits(4)
            ord_nmbr = self.driver.find_element_by_xpath(self.order_title)
            nmbr = ord_nmbr.text
            Ord_Number = str(nmbr.split(" ").pop(1).split("#").pop(1))
            self.write_to_excel("test_review","Order_Number",Ord_Number)
            log.info("Scraped Order number from page and wrote it back to excel")
        except Exception as error:
            log.error(error)

    def clicknext(self):
        log = self.getLogger()
        try:
            self.waits(2)
            self.clickbutton(self.nextbutton)
            log.info("Clicked on next button")
            self.waits(2)
        except Exception as error:
            log.error(error)
