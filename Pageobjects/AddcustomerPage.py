import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver .common.by import By


class AddCustomer:
    lnkCustomer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath="//a[@href='/Admin/Customer/List']"
    btnaddnew_xpath="//a[normalize-space()='Add new']"
    textEmail_xpath="//input[@id='Email']"
    textPassword_xpath="//input[@id='Password']"

    textcustommerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"

    listiteamAdministors_xpath="//span[normalize-space()='Administrators']"

    listiteamRegisterd_xpath="//span[normalize-space()='Registered']"

    listiteamGuest_xpath="//span[normalize-space()='Guests']"

    listiteamvendor_xpath="//span[normalize-space()='Vendors']"
    drpmgrofvendor_xpath="//select[@id='VendorId']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    textFirstName_xpath="//input[@id='FirstName']"
    textLastName_xpath="//input[@id='LastName']"
    textDob_xpath="//input[@id='DateOfBirth']"
    textComanyName_xpath="//input[@id='Company']"
    textAdmContent_xpath="//textarea[@id='AdminComment']"
    btnsave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomermenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def ClickOnCustomerMenuitem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_xpath).click()

    def ClickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnaddnew_xpath).click()

    def setEmail(self,Email):
        self.driver.find_element(By.XPATH,self.textEmail_xpath).send_keys(Email)

    def setPassword(self,Password):
        self.driver.find_element(By.XPATH,self.textPassword_xpath).send_keys(Password)


    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.textcustommerRoles_xpath).click()
        time.sleep(5)
        if role=="Registered":
            self.listiteam=self.driver.find_element(By.XPATH,self.listiteamRegisterd_xpath)
        elif role=="Administrators":
            self.driver.listiteam=self.driver.find_element(By.XPATH,self.listiteamAdministors_xpath)
        elif role== "Guests":
            time.sleep(5)

            self.driver.listiteam=self.driver.find_element(By.XPATH,"//span[normalize-space()='Registered']").click()
            self.listiteam=self.driver.find_element(By.XPATH,self.listiteamGuest_xpath)

        elif role=="Registered":
            self.listiteam=self.driver.find_element(By.XPATH,self.listiteamRegisterd_xpath)
        elif role=="Vendors":
            self.listiteam=self.driver.find_element(By.XPATH,self.listiteamvendor_xpath)
        else:
            self.listiteam=self.driver.find_element(By.XPATH,self.listiteamGuest_xpath)

        time.sleep(5)
        #self.listiteam.click()
        self.driver.execute_script("arguments[0].click();",self.listiteam)

    def setMangerofVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrofvendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,Gender):
        if Gender=="Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif Gender=="Female":
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.textFirstName_xpath).send_keys(fname)

    def setLastName(self, Lname):
        self.driver.find_element(By.XPATH, self.textLastName_xpath).send_keys(Lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.textDob_xpath).send_keys(dob)

    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.textComanyName_xpath).send_keys(company)

    def setAdmincontest(self, contest):
        self.driver.find_element(By.XPATH, self.textAdmContent_xpath).send_keys(contest)


    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath).click()







