import time

import pytest
import self
from selenium import webdriver
from selenium.webdriver import Chrome
from Pageobjects.LoginPage import LoginPages
from Utilities.readproperties import ReadConfig
from Utilities.customloger import LogGen
from Utilities import ExcelUtilities

class Test_002_DDT_login:
    baseURL=ReadConfig.getApplicationURL()
    path=".\\TestData/ExcelUt.xlsx"
    logger=LogGen.loggen()



    def test_Login_ddt(self,setup):
        self.logger.info("**************** Test_002_DDT_login******")
        self.logger.info("**************Home page*******")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPages(self.driver)

        self.rows=ExcelUtilities.getRowCount(self.path,'Sheet1')
        print("Number of rows i a Excel",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.username=ExcelUtilities.readData(self.path,'Sheet1',r,1)
            self.password=ExcelUtilities.readData(self.path,'Sheet1',r,2)
            self.exp=ExcelUtilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(10)


            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("****passed")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                     self.logger.info("******failed******")
                     self.lp.clicklogout()
                     lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=='Pass':
                    self.logger.info("****failed***")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("******passed ******")
                    lst_status.append("Pass")


        if "Fail" not  in lst_status:
            self.logger.info("********Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Login DDT test Failed******")
            self.driver.close()
            assert False

        self.logger.info("***********End ofLogin DDT Test***********")
        self.logger.info("*********** completed TC_LoginDDT_002***********")




