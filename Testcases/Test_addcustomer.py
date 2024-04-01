import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from Pageobjects.LoginPage import LoginPages
from Utilities.readproperties import ReadConfig
from Utilities.customloger import LogGen
from Pageobjects.AddcustomerPage import AddCustomer
import string
import random


class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("**************Test_003_AddCustomer*******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPages(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************Loginsuccessful*******")
        self.logger.info("*********** Starting Add Customer Test********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomermenu()
        self.addcust.ClickOnCustomerMenuitem()

        self.addcust.ClickOnAddnew()

        self.logger.info("*********Providing customer info**********")


        self.Email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.Email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setMangerofVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sandeep")
        self.addcust.setLastName("Kmath")
        self.addcust.setDob("7/05/1992")
        self.addcust.setCompanyName("BusyQ")
        self.addcust.setAdmincontest("This is for testing.....")
        self.addcust.clickOnSave()

        self.logger.info("********saving customer info*****")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully ,' in self.msg:
           assert True==True
        else:
           assert True==False

        self.driver.close()
        self.logger.info("*******Ending Home Page Test**********")





def random_generator(size=10, chars=string.ascii_lowercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))





