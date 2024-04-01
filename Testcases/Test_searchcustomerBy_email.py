import time
import pytest

from Pageobjects.LoginPage import LoginPages
from Pageobjects.SearchcustomerPage import SearchCustomer
from Utilities.readproperties import ReadConfig
from Utilities.customloger import LogGen
from Pageobjects.AddcustomerPage import AddCustomer


class Test_searchcustomerby_email_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()


    def test_customerby_email_004(self,setup):
        self.logger.info("**************Test_003_AddCustomer*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPages(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************Login successful*******")
        self.logger.info("*********** Starting Add Customer Test********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomermenu()
        self.addcust.ClickOnCustomerMenuitem()

        self.logger.info("********Searching customer by emailid**********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickonsearch()
        time.sleep(5)

        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*******************Test_searchcustomerbyemail_004 completed************")
