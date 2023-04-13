import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    lnkCustomer_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_id="Email"
    txtPassword_id="Password"
    txtCustomersRoles_xpath= "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    lstitemAdministrators_xpath="//span[normalize-space()='Administrators']"
    lstitemRegistered_xpath="//span[normalize-space()='Registered']"
    lstitemGuests_xpath="//span[normalize-space()='Guests']"
    lstitemVendors_xpath="//li[@class='k-button k-state-hover']"
    drpmgrOfVendor_xpath="//select[@id='VendorId']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id ="Gender_Female"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath ="//input[@id='LastName']"
    txtDOB_xpath ="//input[@id='DateOfBirth']"
    txtCompanyName_xpath="//input[@id='Company']"
    txtAdminComment_xpath ="//textarea[@id='AdminComment']"
    btnSave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txtCustomersRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Registered']").click()
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def SetfirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def SetLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def SetDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def SetCompanyName(self, cname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(cname)

    def SetAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()




