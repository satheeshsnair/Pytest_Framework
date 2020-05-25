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
        driver = webdriver.Chrome(executable_path="C:\\Users\\satheeshnair\\Desktop\\infocampus\\SourceCode\\AppianJJ\\configuration\\Drivers\\chromedriver.exe")
    elif browser_name == 'ie':
        driver = webdriver.Ie(executable_path="C:\\Users\\satheeshnair\\Desktop\\infocampus\jars\\IEDriverServer.exe")

    driver.get('https://jnjtest.appiancloud.com/suite/portal/login.jsp')
    driver.maximize_window()

    request.cls.driver = driver
    #yield
    #driver.close()