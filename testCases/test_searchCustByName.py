import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.addCustomer import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer

from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_004:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustByEmail(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Arthur")
        searchcust.setLastName("Holmes")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Arthur Holmes")
        assert True==status
        print("test is done")