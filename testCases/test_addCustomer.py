import string
import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.addCustomer import AddCustomer

from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random


class Test_003:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()
        self.email = random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test456")
        self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.SetfirstName("Rohit")
        self.addcust.SetLastName("Kumar")
        self.addcust.SetDob("09/05/1989")
        self.addcust.SetCompanyName("HJUZ")
        self.addcust.SetAdminComment("Hello")
        self.addcust.clickOnSave()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
        else:
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
