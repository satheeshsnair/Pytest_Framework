from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Utilities.baseclass import Baseclass


class Shipto(Baseclass):
    ship_materials_yes = "(//*[@class='RadioSelect---choice_label'])[1]"
    ship_materials_no = "(//*[@class='RadioSelect---choice_label'])[2]"
    jnj_emp_yes = "(//*[@class='RadioSelect---choice_label'])[3]"
    jnj_emp_no = "(//*[@class='RadioSelect---choice_label'])[4]"
    recipient_name = "(//*[@class='TextInput---text TextInput---align_start'])[1]"
    # email = "(//*[@class='TextInput---text TextInput---align_start'])[2]"
    email = "(//*[@class='FieldLayout---input_column']/div/input)[2]"
    office_Phone = "(//*[@class='TextInput---text TextInput---align_start'])[3]"
    expected_date = "(//*[@class='DatePickerWidget---text DatePickerWidget---align_start DatePickerWidget---width_narrow'])"
    is_delivery_yes = "(//*[@class='RadioSelect---choice_label'])[5]"
    is_delivery_no = "(//*[@class='RadioSelect---choice_label'])[6]"
    physical_address_diff_loc = "(//*[@class='DropdownWidget---dropdown_value'])"
    region = "(//*[@class='FieldLayout---input_column']/div/div)[5]"
    country = "(//*[@class='FieldLayout---input_column']/div/div)[6]"
    site_location = "(//*[@class='FieldLayout---input_column']/div/div)[7]"
    street_address = "(//*[@class='FieldLayout---input_column']/div/div)[8]"
    next_button = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])"

    def __init__(self, driver):
        self.driver = driver

    def ship_material(self):
        self.expli_wait(self.ship_materials_yes)
        self.clickbutton(self.ship_materials_yes)

    def usertype(self):
        self.expli_wait(self.jnj_emp_no)
        self.clickbutton(self.jnj_emp_no)

    def recipient(self):
        self.waits(3)
        self.driver.find_element_by_xpath(self.recipient_name).send_keys(self.getdata("test_shipto", "Recipient"))

    def emailid(self):
        self.expli_wait(self.email)
        self.driver.find_element_by_xpath(self.email).send_keys(self.getdata("test_shipto", "Email"))

    def officephone(self):
        self.expli_wait(self.office_Phone)
        self.driver.find_element_by_xpath(self.office_Phone).send_keys(self.getdata("test_shipto", "Office_phone"))

    def expecteddate(self):
        self.waits(2)
        self.driver.find_element_by_xpath(self.expected_date).send_keys("12/31/2020")
        # self.waits(2)
        #         # actions = ActionChains(self.driver)
        #         # actions.send_keys(Keys.ENTER)
        #         # actions.send_keys(Keys.ENTER)
        #         # actions.send_keys(Keys.TAB)

    def is_delivery(self):
        self.waits(1)
        self.clickbutton(self.is_delivery_yes)

    def region_name(self):
        self.waits(2)
        self.get_list_data(self.region, "test_shipto", "Region")

    def country_ship(self):
        self.waits(2)
        self.get_list_data(self.country, "test_shipto", "Country_Ship")

    def site(self):
        self.waits(2)
        self.get_list_data(self.site_location, "test_shipto", "Site_location")

    def street(self):
        self.waits(2)
        self.get_list_data(self.street_address, "test_shipto", "Street")

    def clicknext(self):
        self.waits(1)
        self.clickbutton(self.next_button)
