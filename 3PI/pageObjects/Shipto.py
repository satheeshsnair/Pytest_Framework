from Utilities.baseclass import Baseclass


class Shipto(Baseclass):
    ship_materials_yes = "(//*[@class='RadioSelect---choice_label'])[1]"
    ship_materials_no = "(//*[@class='RadioSelect---choice_label'])[2]"
    jnj_emp_yes = "(//*[@class='RadioSelect---choice_label'])[3]"
    jnj_emp_no = "(//*[@class='RadioSelect---choice_label'])[4]"
    recipient_name = "(//*[@class='TextInput---text TextInput---align_start'])[1]"
    email = "(//*[@class='TextInput---text TextInput---align_start'])[2]"
    office_Phone = "(//*[@class='TextInput---text TextInput---align_start'])[3]"
    expected_date = "(//*[@class='DatePickerWidget---text DatePickerWidget---align_start DatePickerWidget---width_narrow'])"
    is_delivery_yes = "(//*[@class='RadioSelect---choice_label'])[5]"
    is_delivery_no = "(//*[@class='RadioSelect---choice_label'])[6]"
    physical_address_diff_loc = "(//*[@class='DropdownWidget---dropdown_value'])"
    region = "//*[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder']/text()"
    next_button = "(//*[@class='Button---btn Button---default_direction Button---primary appian-context-first-in-list appian-context-last-in-list'])"

    def __init__(self, driver):
        self.driver = driver

    def ship_material(self):
        self.clickbutton(self.ship_materials_yes)

    def usertype(self):
        self.clickbutton(self.jnj_emp_no)

    def recipient(self):
        self.driver.find_element_by_xpath(self.recipient_name).getdata("test_shipto", "Recipient")

    def emailid(self):
        self.driver.find_element_by_xpath(self.email).getdata("test_shipto", "Email")

    def officephone(self):
        self.driver.find_element_by_xpath(self.office_Phone).getdata("test_shipto", "Office_phone")

    def expecteddate(self):
        self.driver.find_element_by_xpath(self.expected_date).getdata("test_shipto", "Expected_date")

    def regions(self):
        self.driver.find_element_by_xpath(self.region).getdata("test_shipto", "Region")

    def country_ship(self):
        self.driver.find_element_by_xpath(self.region).getdata("test_shipto", "Country_Ship")

    def site(self):
        self.driver.find_element_by_xpath(self.region).getdata("test_shipto", "Site_location")

    def street(self):
        self.driver.find_element_by_xpath(self.region).getdata("test_shipto", "Street")

    def clicknext(self):
        self.waits(1)
        self.clickbutton(self.next_button)
