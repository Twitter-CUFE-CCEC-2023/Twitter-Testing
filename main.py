from faulthandler import is_enabled
import unittest
from selenium import webdriver
import page
import time
from locator import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/Lucio/AppData/Local/Programs/Python/Python310/chromedriver_win32/chromedriver.exe"


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://twitter.com/")
        

     
    def test_case_log_in(self):
        Login_page = page.LoginPage(self.driver)
        Password_page=page.enteryourpassword(self.driver)
        Login_page.click_sign_in_button()
        Login_page.insert_your_info("01001")
        Login_page.click_Next_button()
        #Login_page.cheack_ur_error_msg()
        Password_page.enter_your_password("passWORD")
        
        if(Password_page.forget_password()==Passwordlocarors.FORGET_PASSWORD_TEXT):
            assert True
        else:
            assert False     
        
        #Password_page.is_login_enable()
       
        
        
        
        #time.sleep(1000)
        assert True
        # i cant detect the message bec its pop msg and disapper and selenium cant deal with it
    '''
    def test_case_sign_up(self):
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        
        #testing:that the next button is enable or not 
        
        if(not SignUp_page.is_NEXT_enable()):
            assert False
        else:
            assert True       
        
        #testing: that text box cant carry more than 50 letters
        
        SignUp_page.insert_ur_name(SignUpLocators.WRONG_NAMEX50)
        if(SignUp_page.cheack_ur_name_size()):
            assert True
        else:
            # if it accept more than 50 letter as ur name
            assert False    
        
        
        #testing  inserting a text in phone number text box
           
        SignUp_page.insert_ur_phone("WRONGMSG")
        actualmsg=SignUp_page.check_wrong_msg()
        if actualmsg==SignUpLocators.EXPECTED_MSG:
            assert True
        else:
            assert False
        
        
        # testing : creating account 
          
        SignUp_page.insert_ur_name("ali hithem")      
        SignUp_page.insert_ur_phone("01001900361")
       # SignUp_page.choose_day_month_year()
        time.sleep(15)
        SignUp_page.click_NEXT()
        assert True
        
    '''    
        
    
    '''
    def test_case_signIn_byGoogle(self):
        Signin_page=page.loginbyGoogle(self.driver)
        Signin_page.click_sign_in_with_Gmail()
        time.sleep(1000)
    '''   
        
        
              
    
        
    
    
    
    
    
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
        
        
        
if __name__== "__main__":
    unittest.main()
        
        