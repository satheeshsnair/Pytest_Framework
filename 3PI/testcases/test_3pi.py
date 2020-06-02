import pytest

from Utilities.baseclass import Baseclass
from pageObjects.Actionstab import ActionsTab
from pageObjects.CreateRequestPage import CreateReq
from pageObjects.Loginpage import LoginPage
from pageObjects.Newstab import NewsTab
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

    def test_selectOrderType(self):
        log = self.getLogger()
        createreq = CreateReq(self.driver)
        createreq.selectOrdertype()
        log.info("Selected Dropdown option")
        createreq.clicknext()
        self.waits(3)
        title = self.driver.title
        assert title == "Submit Order Server"
        createreq.clicknext()
        self.waits(3)
        log.info("Navigated to project page ")

    def test_Orderdetails(self):
        log = self.getLogger()
        createreq = CreateReq(self.driver)
        createreq.project()
        self.waits(3)
        title = self.driver.title
        assert title == "Submit Order Server"
        createreq.clicknext()
        self.waits(3)
        log.info("Navigated to Financial info")

    def test_projectinfo(self):
        log = self.getLogger()
        createreq = CreateReq(self.driver)
        createreq.prjinfo()
        log.info("Entered all data")
        createreq.clicknext()
        self.waits(1)
        title = self.driver.title
        assert title == "Submit Order Server"
        self.waits(1)
        log.info("Navigated to Ship to page")

    def ship_to(self):
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
