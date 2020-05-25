import time

from Utilities.baseclass import Baseclass
from pageObjects.Actionstab import ActionsTab
from pageObjects.CreateRequestPage import CreateReq
from pageObjects.Loginpage import LoginPage
from pageObjects.Newstab import NewsTab
from selenium.webdriver.support.select import Select


class TestE2e(Baseclass):

    def test_login(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        # loginpage.login()
        loginpage.getusername()
        loginpage.getpassword()
        loginpage.signinbutton()
        log.info("logged in suucessfully")
        self.waits()

    def test_clickAction(self):
        log = self.getLogger()
        newstab = NewsTab(self.driver)
        newstab.clickonActiontab()
        log.info("Clicked on Actions Tab")
        self.waits()

    def test_submitorderreq(self):
        log = self.getLogger()
        actionstab = ActionsTab(self.driver)
        self.verifylinkpresent("3PI Submit Order Request")
        actionstab.clickon3PISubmitOrderRequest()
        log.info("Clicked on 3PI Submit Order Request")
        self.waits()

    def test_selectOrderType(self):
        log = self.getLogger()
        createreq = CreateReq(self.driver)
        self.waits()
        createreq.selectOrdertype()
        # self.selectOptionByText(createreq.selectOrdertype(),"Server")
        log.info("Selected Dropdown option")
        # self.selectOptionByText(createreq.selectOrdertype(),"Server")
        # paths = self.driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder']")
        # sel = Select(paths)
        # sel.select_by_visible_text("Server")