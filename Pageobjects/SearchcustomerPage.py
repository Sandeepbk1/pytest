from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

class SearchCustomer:
    textboxEmail_id="SearchEmail"
    textboxFname_id="SearchFirstName"
    textboxLname_id="SearchLastName"
    buttonsearch_id="search-customers"

    table_xpath="//div[@class='row']//div[@class='col-md-12']"

    row_xpath="//tbody/tr[]"
    col_xpath="//div[@class='col-md-12']"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,eamil):
        self.driver.find_element(By.ID, self.textboxEmail_id).clear()
        self.driver.find_element(By.ID,self.textboxEmail_id).send_keys(eamil)

    def setFname(self,firstname):
        self.driver.find_element(By.ID, self.textboxFname_id).clear()
        self.driver.find_element(By.ID,self.textboxFname_id).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.ID, self.textboxLname_id).clear()
        self.driver.find_element(By.ID,self.textboxLname_id).send_keys(lastname)

    def clickonsearch(self):
        self.driver.find_element(By.ID,self.buttonsearch_id).click()

    def getNorows(self):
        return len(self.driver.find_element(By.XPATH,self.row_xpath))


    def getNocolumn(self):
        return len(self.driver.find_element(By.XPATH,self.col_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNorows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//td[normalize-space()='victoria_victoria@nopCommerce.com']").text
            if emailid==email:
                flag=True
                break
        return flag




