import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

list = []
list2 = []
#chrome
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:\\Users\satheeshnair\Desktop\infocampus\SourceCode\AppianJJ\configuration\Drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/") #get url
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
#time.sleep(4)
count=len(driver.find_elements_by_xpath("//*[@class='product']"))

assert count == 3
time.sleep(5)
buttons = driver.find_elements_by_xpath("//*[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element_by_xpath("//*[@class='cart-icon']/img").click()
driver.find_element_by_xpath("(//*[@class='action-block']/button)[1]").click()
time.sleep(5)
veggies = driver.find_elements_by_xpath("//*[@class='product-name']")
for veg in veggies:
    list2.append(veg.text)

print(list2)
assert list == list2
time.sleep(2)
original = driver.find_element_by_xpath("//*[@class='discountAmt']").text
driver.find_element_by_xpath("//*[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//*[@class='promoBtn']").click()
time.sleep(6)
dis = driver.find_element_by_xpath("//*[@class='discountAmt']").text
print(original,dis)
assert float(dis) < int(original)
print(driver.find_element_by_xpath("//*[@class='promoInfo']").text)

values = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for value in values:
    sum = sum + int(value.text)
print(sum)

total_amt = int(driver.find_element_by_xpath("//*[@class='totAmt']").text)
print(total_amt)
assert  sum == total_amt


