from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

serv_obj = Service("C:\drivers selenium\chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=serv_obj)


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=serv_obj)
        print("launching Chrome")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("launching Firefox")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####HTML####
def pytest_configure(config):
    config._metadata['Project Name'] = "NOP COMMERCE"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester'] = "Jhansi"


pytest.hookimpl(optionalhook=True)


def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
