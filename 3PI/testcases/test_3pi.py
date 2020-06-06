import pytest

from utilities.baseclass import Baseclass
from pageObjects.Actionstab import ActionsTab
from pageObjects.Financial_Info import Financial_Info
from pageObjects.Loginpage import LoginPage
from pageObjects.Newstab import NewsTab
from pageObjects.OrderDetails import Orderdetails
from pageObjects.OrderInfo import Orderinfo
from pageObjects.Review import Review
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
            log.info("logged in successful")
            self.Pass_snaps("login")
        else :
            log.info("logged in failed")
            self.Fail_snaps("login_failed")
            assert False

    def test_clickAction(self):
        log = self.getLogger()
        newstab = NewsTab(self.driver)
        newstab.clickonActiontab()
        self.waits(3)
        title = self.driver.title
        if title == "Actions" :
            assert True
            log.info("Navigated to Actions Tab")
            self.Pass_snaps("Actions Tab displayed")
        else :
            log.info("failed to click on actions tab")
            self.Fail_snaps("Actions tab not clicked")
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
            log.info("Click on Submit request link")
            self.Pass_snaps("Submit order request link clicked and Order info screen displayed")
        else:
            log.info("failed to click on submit request link")
            self.Fail_snaps("failed to click on submit request link")

    def test_orderinfo(self):
        log = self.getLogger()
        orderinfo = Orderinfo(self.driver)
        orderinfo.selectOrdertype()
        self.Pass_snaps("Order type")
        orderinfo.clicknext()
        self.waits(2)
        title = self.driver.title
        if title == "Submit Order Server":
            orderinfo.clicknext()
            self.Pass_snaps("Order type selected")
        else :
            log.info("Not able to navigate to Order details page")
            self.Fail_snaps("Not able to navigate to Order details page")
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
            self.Pass_snaps("Navigated to Financial info")
        else :
            log.info("Failed to navigate to Financial info")
            self.Fail_snaps("Failed to navigate to Financial info")
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
            self.Pass_snaps("Navigated to Ship to page")
        else :
            log.info("Not able to navigate to Ship to page")
            self.Fail_snaps("Not able to navigate to Ship to page")
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
            self.Pass_snaps("Navigating to Review page")
        else :
            log.info("Failed to enter review page")
            self.Fail_snaps("Failed to enter review page")
            assert False

    def test_review_page(self):
        log = self.getLogger()
        review = Review(self.driver)
        review.get_Order_title()
        review.clicknext()
        self.waits(3)
        title = self.driver.title
        if title == "Actions" :
            assert True
            log.info("Order has been submitted successfully")
            self.Pass_snaps("Order has been submitted successfully")
        else :
            log.info("Order submitting failed")
            self.Fail_snaps("Order submitting failed")
            assert False