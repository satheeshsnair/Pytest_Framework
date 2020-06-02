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
        # loginpage.login()
        loginpage.getusername()
        loginpage.getpassword()
        loginpage.signinbutton()
        self.waits(3)
        title = self.driver.title
        assert title == "News"
        log.info("logged in successfully")

    def test_clickAction(self):
        log = self.getLogger()
        newstab = NewsTab(self.driver)
        newstab.clickonActiontab()
        self.waits(3)
        title = self.driver.title
        assert title == "Actions"
        log.info("Clicked on Actions Tab")

    def test_submitorderreq(self):
        log = self.getLogger()
        actionstab = ActionsTab(self.driver)
        self.verifylinkpresent("3PI Submit Order Request")
        actionstab.clickon3PISubmitOrderRequest()
        self.waits(3)
        title = self.driver.title
        assert title == "Generate Order Request"
        log.info("Clicked on 3PI Submit Order Request")

    def test_orderinfo(self):
        log = self.getLogger()
        orderinfo = Orderinfo(self.driver)
        orderinfo.selectOrdertype()
        orderinfo.clicknext()
        self.waits(2)
        title = self.driver.title
        assert title == "Submit Order Server"
        orderinfo.clicknext()
        self.waits(1)
        log.info("Navigated to Order details page")

    def test_OrderDetails(self):
        log = self.getLogger()
        orderdetails = Orderdetails(self.driver)
        orderdetails.project()
        self.waits(1)
        orderdetails.select_project()
        title = self.driver.title
        assert title == "Submit Order Server"
        log.info("Navigated to Financial info")

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
        assert title == "Submit Order Server"
        self.waits(1)
        log.info("Navigated to Ship to page")

    def test_ship_to(self):
        log = self.getLogger()
        shipto = Shipto(self.driver)
        shipto.ship_material()
        shipto.usertype()
        shipto.recipient()
        shipto.emailid()
        shipto.officephone()
        shipto.expecteddate()
        shipto.regions()
        shipto.country_ship()
        shipto.site()
        shipto.street()
        shipto.clicknext()
        title = self.driver.title
        assert title == "Submit Order Server"
        self.waits(1)
        log.info("Enetred shiiping info. Navigating to review page")
