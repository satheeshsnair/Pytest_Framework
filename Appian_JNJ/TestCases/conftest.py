import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=r"C:\Users\satheeshnair\Desktop\infocampus\SourceCode\AppianJJ\configuration\Drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get('https://jnjtest.appiancloud.com/suite/portal/login.jsp')
    request.cls.driver = driver
    yield
    driver.close()










