from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from utilities.baseclass import Baseclass


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
        log = self.getLogger()
        try:
            self.expli_wait(self.ship_materials_yes)
            self.clickbutton(self.ship_materials_yes)
            log.info("Clicked on ship material radio button")
        except Exception as error:
            log.error(error)

    def usertype(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.jnj_emp_no)
            self.clickbutton(self.jnj_emp_no)
            log.info("Clicked on jnj employee radio button")
        except Exception as error:
            log.error(error)

    def recipient(self):
        log = self.getLogger()
        try:
            self.waits(3)
            self.driver.find_element_by_xpath(self.recipient_name).send_keys(self.getdata("test_shipto", "Recipient"))
            log.info("Entered Recipient")
        except Exception as error:
            log.error(error)


    def emailid(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.email)
            self.driver.find_element_by_xpath(self.email).send_keys(self.getdata("test_shipto", "Email"))
            log.info("Entered Email")
        except Exception as error:
            log.error(error)

    def officephone(self):
        log = self.getLogger()
        try:
            self.expli_wait(self.office_Phone)
            self.driver.find_element_by_xpath(self.office_Phone).send_keys(self.getdata("test_shipto", "Office_phone"))
            log.info("Entered Office phone")
        except Exception as error:
            log.error(error)

    def expecteddate(self):
        log = self.getLogger()
        try:
            self.waits(2)
            self.driver.find_element_by_xpath(self.expected_date).send_keys("12/31/2020")
            log.info("Entered date")
        except Exception as error:
            log.error(error)

    def is_delivery(self):
        log = self.getLogger()
        try:
            self.waits(1)
            self.clickbutton(self.is_delivery_yes)
            log.info("Selected Delivery radio button")
        except Exception as error:
            log.error(error)

    def region_name(self):
        log = self.getLogger()
        try:
            self.waits(2)
            self.get_list_data(self.region, "test_shipto", "Region")
            log.info("Entered Region")
        except Exception as error:
            log.error(error)

    def country_ship(self):
        log = self.getLogger()
        try:
            self.waits(2)
            self.get_list_data(self.country, "test_shipto", "Country_Ship")
            log.info("Entered Country to ship")
        except Exception as error:
            log.error(error)

    def site(self):
        log = self.getLogger()
        try:
            self.waits(1)
            self.get_list_data(self.site_location, "test_shipto", "Site_location")
            log.info("Entered Site")
        except Exception as error:
            log.error(error)

    def street(self):
        log = self.getLogger()
        try:
            self.waits(1)
            self.get_list_data(self.street_address, "test_shipto", "Street")
            log.info("Entered Street")
            self.Pass_snaps("Entered all the required data in Financial info page")
        except Exception as error:
            log.error(error)

    def clicknext(self):
        log = self.getLogger()
        try:
            self.waits(1)
            self.clickbutton(self.next_button)
            log.info("Clicked on next button")
        except Exception as error:
            log.error(error)