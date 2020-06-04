from Utilities.baseclass import Baseclass


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
        self.expli_wait(self.country)
        self.get_list_data(self.country, "test_projectinfo", "country")

    def capital_amt(self):
        self.expli_wait(self.capital)
        self.driver.find_element_by_xpath(self.capital).send_keys(self.getdata("test_projectinfo", "Capital Amount"))

    def expense_amount(self):
        self.expli_wait(self.expense)
        self.driver.find_element_by_xpath(self.expense).send_keys(self.getdata("test_projectinfo", "Expense Amount"))

    def quote_nmbr(self):
        self.expli_wait(self.quote)
        self.driver.find_element_by_xpath(self.quote).send_keys(self.getdata("test_projectinfo", "Quote Number"))

    def supplier_name(self):
        self.expli_wait(self.supplier)
        self.get_list_data(self.supplier, "test_projectinfo", "Supplier")

    def upload_file(self):
        self.expli_wait(self.upload)
        self.uploadfile(self.upload, self.getdata("test_projectinfo", "path"))
        self.waits(2)

    def click_next(self):
        self.driver.find_element_by_xpath(self.nextbutton).click()