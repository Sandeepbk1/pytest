import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from Pageobjects.LoginPage import LoginPages
from Utilities.readproperties import ReadConfig
from Utilities.customloger import LogGen

class Test_001_login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()


    logger=LogGen.loggen()

    def test_HomepageTitle(self,setup):

        self.logger.info("**************Home page*******")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots"+" test_HomepageTitle.png")
            self.driver.close()
            assert False


    def test_Login(self,setup):
        self.logger.info("**************Home page*******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPages(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************test passed*******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + " test_Login.png")
            self.driver.close()
            assert False