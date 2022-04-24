from faulthandler import is_enabled
from lib2to3.pgen2 import driver
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
testcases=0
passed=0
falied=0

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.twittercloneteamone.tk/")
        

    ''' 
    def test_case_log_in(self):
        Login_page = page.LoginPage(self.driver)
        Password_page=page.enteryourpassword(self.driver)
        Login_page.click_sign_in_button()
        Login_page.insert_your_info("01001")
        Login_page.click_Next_button()
        #Login_page.cheack_ur_error_msg()
        
        if(not Password_page.is_login_enable()):
            assert False
        else:
            assert True 
          
        Password_page.enter_your_password("passWORD")
        
        if(Password_page.forget_password()==Passwordlocarors.FORGET_PASSWORD_TEXT):
            assert True
        else:
            assert False   
          
        Password_page.click_login()
        assert True
        '''
        
        
        
        
       # 'div[data-testid="toast"]'
   # <div role="alert" class="css-1dbjc4n r-1awozwy r-1kihuf0 r-l5o3uw r-z2wwpe r-18u37iz r-1wtj0ep r-zd98yo r-xyw6el" data-testid="toast" xpath="1"><div dir="auto" class="css-901oao r-jwli3a r-1wbh5a2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-1e081e0 r-qvutc0"><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">Sorry, we could not find your account.</span></div><div aria-hidden="true" class="css-1dbjc4n r-18u37iz"></div></div>
        
        
        
        #time.sleep(1000)
       # assert True
    '''   
    def test_case_SIGNUP_click_sign_up_button(self):
        SignUp_page=page.SignUpPage(self.driver)
        if(SignUp_page.click_sign_up()):
            assert True
        else:
            assert False    
    '''    
        #testing:that the next button is enable or not    # i cant detect the message bec its pop msg and disapper and selenium cant deal with it
    '''
    def test_case_SIGNUP_is_next_Enable(self):
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        #testing:that the next button is enable or not 
        if(SignUp_page.is_NEXT_enable()):
            assert False
        else:
            assert True       
    '''    
        #testing: that text box cant carry more than 50 letters
    '''       
    def test_case_SIGNUP_textboxX50(self): 
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()   
        SignUp_page.insert_ur_name(SignUpLocators.WRONG_NAMEX50)
        if(SignUp_page.cheack_ur_name_size()):
            assert True
        else:
            # if it more than 50 letter as ur name
            assert False    
    '''       
    '''      
        #testing  inserting a wrong email address text box
    def test_case_SIGNUP__wrong_email(self): 
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()       
        SignUp_page.insert_ur_email("1234")
        actualmsg=SignUp_page.check_wrong_msg_email()
        print(actualmsg)
        if actualmsg==SignUpLocators.EXPECTED_MSG_EMAIL:
            assert True
        else:
            assert False
     '''        
    '''
    def test_case_SIGNUP_phone_link_text(self):
       SignUp_page=page.SignUpPage(self.driver)
       SignUp_page.click_sign_up()
       if SignUpLocators.PHONE_LINK_TEXT==SignUp_page.check_phone_link():
            assert True
       else:
           assert False 
    '''
    '''       
    def test_case_SIGNUP_wrong_phone_number(self):
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.click_phone_link()
        SignUp_page.insert_ur_phone(SignUpLocators.WRONG_NAMEX50)
        if SignUpLocators.ERROR_MSG_EMAIL==SignUp_page.check_wrong_msg_email():
            assert True
        else:
            assert False    
    ''' 
    '''    
    def test_case_SIGNUP_next_enable_after_inserting_wrong_phone(self):
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.click_phone_link()
        SignUp_page.insert_ur_phone(SignUpLocators.WRONG_NAMEX50)
        SignUp_page.insert_ur_name("testing")
        if(SignUp_page.is_NEXT_enable()):
            assert False
        else:
            assert True 
    '''
    '''
    def test_case_SIGNUP_cheack_email_link(self):
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.click_phone_link()
        if SignUpLocators.EMAIL_LINK_TEXT==SignUp_page.check_Email_link():
            assert True
        else:
            assert False    
    '''     
                  
    '''    
    def test_case_SIGNUP_choose_date(self): 
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
            
    '''         
        
    '''    
    def test_case_SIGNUP_create_account(self): 
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        #when i click on the link it clear my name      
        SignUp_page.insert_ur_name("testing")
        SignUp_page.click_phone_link()      
        SignUp_page.insert_ur_phone("01001729999") 
       # SignUp_page.choose_day_month_year()
        SignUp_page.click_NEXT()
        assert True
    '''    
    '''   
    def test_case_SIGNIN_click_the_button(self):
        Signin_page=page.SignInPage(self.driver)
        if Signin_page.click_sign_in_button():
            assert True
        else:
            assert False    
    '''
    '''
    def test_case_SIGNIN_check_error_msg(self):
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(5)
        Signin_page.click_Next_button()
        if Signin_page.check_alert_msg()==SignInLocators.ALERT_MSG_TEXT:
            assert True
        else:
            assert False    
    ''' 
    '''    
    def test_case_SIGNIN_login_enable(self):
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        Signin_page.insert_your_info("testing")
        Signin_page.click_Next_button()
        time.sleep(2)
        if (not Signin_page.is_login_button_enable()):
            assert False
        else:
            assert True    
    '''
    '''
    def test_case_SIGNIN_check_wrong_pass(self):
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        Signin_page.insert_your_info("testing")
        Signin_page.click_Next_button()
        Signin_page.insert_your_password("wrong password")
        time.sleep(2)
        Signin_page.click_login()
        if Signin_page.check_error_msg_of_wrong_password()==SignInLocators.WRONG_PASSWORD_TEXT:
            assert True
        else:
            assert False    
    '''
    '''
    def test_case_SIGNIN_FORGET_PASSWORD_forget_password(self):
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(2)
        Signin_page.click_forget_password()
        if Signin_page.foregt_ur_password_insert_info("Wrong password"):
            assert True
        else:
            assert False    
    '''
    '''
    def test_case_SIGNIN_signup(self):
        Signin_page=page.SignInPage(self.driver)
        SignUp_page=page.SignUpPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(2)
        Signin_page.click_signup()
        if SignUp_page.insert_ur_name("testing"):
            assert True
        else:
            assert False    
        
    '''    
    '''  
    def test_case_SIGNIN_FORGET_PASSWORD_forget_password(self):
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(2)
        Signin_page.click_signin_with_google()
        if Signin_page.insert_ur_Gmail("testing"):
            assert True
        else:
            assert False                        
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
        
        