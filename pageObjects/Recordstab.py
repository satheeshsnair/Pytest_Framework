from utilities.baseclass import Baseclass


class RecordsTab(Baseclass):

    def __init__(self,driver):
        self.driver = driver

    orderrequest = "(//*[@class='ContentLayout---content_layout ContentLayout---padding_less'])[2]"

    def clickonorderreq(self):
        log = self.getLogger()
        try:
            # self.driver.find_element(self.orderrequest).click()
            self.clickbutton(self.orderrequest)
            log.info("Clicked on 3PI Order Request")
        except Exception as error:
            log.error(error)