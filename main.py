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
        

    ''' 
    def test_case_log_in(self):
        Login_page = page.LoginPage(self.driver)
        Login_page.click_sign_in_button()
        Login_page.insert_your_info("01001900361")
        Login_page.click_Next_button()
        Login_page.cheack_ur_error_msg()
        
        time.sleep(1000)
        assert True
        # i cant detect the message bec its pop msg and disapper and selenium cant deal with it
    
    def test_case_sign_up(self):
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.insert_ur_name(SignUpLocators.WRONG_NAMEX50)
        if(SignUp_page.cheack_ur_name_size()):
            assert True
        else:
            # if it accept more than 50 letter as ur name
            assert False    
        
        print(SignUp_page.click_NEXT())       
        SignUp_page.insert_ur_phone("WRONGMSG")
        actualmsg=SignUp_page.check_wrong_msg()
        if actualmsg==SignUpLocators.EXPECTED_MSG:
            assert True
        else:
            assert False
        SignUp_page.insert_ur_name("ali hithem")      
        SignUp_page.insert_ur_phone("01001900361")
       # SignUp_page.choose_day_month_year()
        time.sleep(15)
        SignUp_page.click_NEXT()
        
        
    '''
    def test_case_signIn_byGoogle(self):
        Signin_page=page.loginbyGoogle(self.driver)
        Signin_page.click_sign_in_with_Gmail()
        time.sleep(1000)
       
        
        
              
    
        
    
    
    
    
    
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
        
        
        
if __name__== "__main__":
    unittest.main()
        
        