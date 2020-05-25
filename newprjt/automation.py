import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\satheeshnair\Desktop\infocampus\SourceCode\AppianJJ\configuration\Drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/") #get url
driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
products = driver.find_elements_by_xpath("//*[@class='card h-100']")
for product in products:
    prod_name=product.find_element_by_xpath("div/h4/a").text
    if prod_name == "Blackberry":
        product.find_element_by_xpath("div[2]/button").click()

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_xpath("//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
success_text = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you! " in success_text

driver.get_screenshot_as_file("screen.png")