from utilities.baseclass import Baseclass


class Financial_Info(Baseclass):
    country = "(//div[@class='FieldLayout---input_column']/div/div)[1]"
    supplier = "(//div[@class='FieldLayout---input_column']/div/div)[3]"
    capital = "(//*[@class='TextInput---text TextInput---align_start'])[3]"
    expense = "(//*[@class='TextInput---text TextInput---align_start'])[4]"
    quote = "(//*[@class='TextInput---text TextInput---align_start'])[5]"
    upload = "//*[@class='FileUploadWidget---ui-inaccessible']"
    docname = ("//*[@class='FileUploadWidget---upload_item']/div[2]/p/strong")
    nextbutton = "//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list']"

    def __init__(self,driver):
        self.driver = driver

    def country_name(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.country)
            self.get_list_data(self.country, "test_projectinfo", "country")
            log.info("Country selected")
        except Exception as error:
            log.error(error)

    def capital_amt(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.capital)
            self.driver.find_element_by_xpath(self.capital).send_keys(self.getdata("test_projectinfo", "Capital Amount"))
            log.info("Entered amount")
        except Exception as error:
            log.error(error)

    def expense_amount(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.expense)
            self.driver.find_element_by_xpath(self.expense).send_keys(self.getdata("test_projectinfo", "Expense Amount"))
            log.info("Entered expense amount")
        except Exception as error:
            log.error(error)

    def quote_nmbr(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.quote)
            self.driver.find_element_by_xpath(self.quote).send_keys(self.getdata("test_projectinfo", "Quote Number"))
            log.info("Entered quote number")
        except Exception as error:
            log.error(error)

    def supplier_name(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.supplier)
            self.get_list_data(self.supplier, "test_projectinfo", "Supplier")
            log.info("Entered supplier")
        except Exception as error:
            log.error(error)

    def upload_file(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.upload)
            self.uploadfile(self.upload, self.getdata("test_projectinfo", "path"))
            self.waits(2)
            log.info("Uploaded file")
            self.Pass_snaps("Entered data in Financial info tab")
        except Exception as error:
            log.error(error)

    def click_next(self):
        log = self.getLogger()
        try:
            self.driver.find_element_by_xpath(self.nextbutton).click()
            log.info("Clicked on nesxt button")
        except Exception as error:
            log.error(error)