import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtilis


class Test_001:
    base_url = ReadConfig.getApplicationURL()
    path = ".//TestData/book1.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******Test_login****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtilis.getRowCount(self.path, 'Sheet1')
        print("Number of rows", self.rows)

        lst_status = []  # empty list

        for r in range(2, self.rows+1):
            self.user = XLUtilis.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilis.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilis.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == "fail":
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    lst_status.append("Fail")
                elif self.exp == "fail":
                    lst_status.append("Pass")