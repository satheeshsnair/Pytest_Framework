import time
import subprocess

import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path = "../driver/chromedriver.exe")
    elif browser_name == 'ie':
        driver = webdriver.Ie(executable_path = "../driver/IEDriverServer.exe")

    driver.maximize_window()
    driver.get('https://jnjtest.appiancloud.com/suite/portal/login.jsp')

    request.cls.driver = driver

    yield
    time.sleep(2)
    driver.close()
    subprocess.call("taskkill /f /IM chromedriver.exe")
