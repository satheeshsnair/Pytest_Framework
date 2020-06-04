import pytest

from Utilities.baseclass import Baseclass
from pageObjects.Actionstab import ActionsTab
from pageObjects.CreateRequestPage import CreateReq
from pageObjects.Financial_Info import Financial_Info
from pageObjects.Loginpage import LoginPage
from pageObjects.Newstab import NewsTab
from pageObjects.OrderDetails import Orderdetails
from pageObjects.OrderInfo import Orderinfo
from pageObjects.Shipto import Shipto


class TestE2e(Baseclass):

    def test_login(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.getusername()
        loginpage.getpassword()
        loginpage.signinbutton()
        self.waits(3)
        title = self.driver.title
        if title == "News":
            assert True
            log.info("logged in successfully")
        else :
            log.info("logged in failed")
            assert False

    def test_clickAction(self):
        log = self.getLogger()
        newstab = NewsTab(self.driver)
        newstab.clickonActiontab()
        self.waits(3)
        title = self.driver.title
        if title == "Actions" :
            assert True
            log.info("Clicked on Actions Tab")
        else :
            log.info("Failed to click on Actions Tab")
            assert False

    def test_submitorderreq(self):
        log = self.getLogger()
        actionstab = ActionsTab(self.driver)
        self.verifylinkpresent("3PI Submit Order Request")
        actionstab.clickon3PISubmitOrderRequest()
        self.waits(3)
        title = self.driver.title
        if title == "Generate Order Request" :
            assert True
            log.info("Clicked on 3PI Submit Order Request")
        else :
            log.info("Failed to click on 3PI Submit Order Request")
            assert False

    def test_orderinfo(self):
        log = self.getLogger()
        orderinfo = Orderinfo(self.driver)
        orderinfo.selectOrdertype()
        orderinfo.clicknext()
        self.waits(2)
        title = self.driver.title
        if title == "Submit Order Server":
            orderinfo.clicknext()
            self.waits(1)
            log.info("Navigated to Order details page")
        else :
            log.info("Not able to navigate to Order details page")
            assert False

    def test_OrderDetails(self):
        log = self.getLogger()
        orderdetails = Orderdetails(self.driver)
        orderdetails.project()
        self.waits(1)
        orderdetails.select_project()
        title = self.driver.title
        if title == "Submit Order Server":
            assert  True
            log.info("Navigated to Financial info")
        else :
            log.info("Not able to navigate to Financial info")
            assert False

    def test_financial(self):
        log = self.getLogger()
        finance = Financial_Info(self.driver)
        finance.country_name()
        finance.capital_amt()
        finance.expense_amount()
        finance.quote_nmbr()
        finance.supplier_name()
        finance.upload_file()
        finance.click_next()
        self.waits(2)
        title = self.driver.title
        if title == "Submit Order Server" :
            assert True
            log.info("Navigated to Ship to page")
        else :
            log.info("Not able to navigate to Ship to page")
            assert False

    def test_ship_to(self):
        log = self.getLogger()
        shipto = Shipto(self.driver)
        shipto.ship_material()
        shipto.usertype()
        shipto.recipient()
        shipto.emailid()
        shipto.officephone()
        shipto.is_delivery()
        shipto.expecteddate()
        shipto.region_name()
        shipto.country_ship()
        shipto.site()
        shipto.street()
        shipto.clicknext()
        title = self.driver.title
        if title == "Submit Order Server" :
            assert True
            log.info("Entered shipping info. Navigating to review page")
        else :
            log.info("Failed to enter review page")
            assert False