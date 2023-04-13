import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage(self,setup):
        self.logger.info("******Test_homepage****")
        self.logger.info("******verifying****")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******Test passed ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage.png")
            self.driver.close()
            self.logger.info("******Test_failed****")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******Test_login****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.lp.clicklogout()
            self.logger.info("******Test passed ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("******Test failed ****")
            assert False

