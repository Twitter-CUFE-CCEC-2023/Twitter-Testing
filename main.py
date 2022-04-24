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
failed=0
STARTUP_PAGE="http://www.twittercloneteamone.tk/"
HOME_PAGE="http://www.twittercloneteamone.tk/home"
Report = open("project_log.txt", "a")
class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(STARTUP_PAGE)
        

   

 
    def test_case_SIGNUP_click_sign_up_button(self):
        SignUp_page=page.SignUpPage(self.driver)
        global testcases
        global passed
        global failed
        testcases+=1
        #Report.write("test case=>",testcases)
        Report.write("SIGN UP PAGE -> test case of Sign up button \n" )
        
        if(SignUp_page.click_sign_up()):
            passed+=1
            Report.write("PASSED\n\n")
            assert True         
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
        
        #testing:that the next button is enable or not    # i cant detect the message bec its pop msg and disapper and selenium cant deal with it
    
    
    def test_case_SIGNUP_is_next_Enable(self):
        global testcases
        global passed
        global failed
        testcases+=1
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        Report.write("SIGN UP PAGE -> test case of is next button is enable without inserting info. \n" )
        #testing:that the next button is enable or not 
        if(SignUp_page.is_NEXT_enable()):
            failed+=1
            Report.write("FAILED\n\n")
            assert False
        else:
            passed+=1
            Report.write("PASSED\n\n")
            assert True       
        
        #testing: that text box cant carry more than 50 letters
          
    def test_case_SIGNUP_textboxX50(self): 
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of inserting more than 50 letter in the textbox of the Name \n" )
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()   
        SignUp_page.insert_ur_name(SignUpLocators.WRONG_NAMEX50)
        if(SignUp_page.cheack_ur_name_size()):
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            # if it more than 50 letter as ur name
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
           
         
        #testing  inserting a wrong email address text box
    def test_case_SIGNUP__wrong_email(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of inserting wrong email \n" ) 
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()       
        SignUp_page.insert_ur_email("1234")
        actualmsg=SignUp_page.check_wrong_msg_email()
        print(actualmsg)
        if actualmsg==SignUpLocators.EXPECTED_MSG_EMAIL:
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False
            
    
    def test_case_SIGNUP_phone_link_text(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of check text of phone link \n" )
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        if SignUpLocators.PHONE_LINK_TEXT==SignUp_page.check_phone_link():
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False 
    
           
    def test_case_SIGNUP_wrong_phone_number(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of inserting wrong number \n" )
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.click_phone_link()
        SignUp_page.insert_ur_phone(SignUpLocators.WRONG_NAMEX50)
        if SignUpLocators.ERROR_MSG_EMAIL==SignUp_page.check_wrong_msg_email():
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
     
       
    def test_case_SIGNUP_next_enable_after_inserting_wrong_phone(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of checking the next button after inserting wrong phone number \n" )
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.click_phone_link()
        SignUp_page.insert_ur_phone(SignUpLocators.WRONG_NAMEX50)
        SignUp_page.insert_ur_name("testing")
        if(SignUp_page.is_NEXT_enable()):
            failed+=1
            Report.write("FAILED\n\n")
            assert False
        else:
            passed+=1
            Report.write("PASSED\n\n")
            assert True 
    
    
    def test_case_SIGNUP_cheack_email_link(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of format of  Email link \n" )
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        SignUp_page.click_phone_link()
        if SignUpLocators.EMAIL_LINK_TEXT==SignUp_page.check_Email_link():
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
         
                   
    '''    
    def test_case_SIGNUP_choose_date(self): 
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
            
    '''         
        
    
    def test_case_SIGNUP_create_account(self): 
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN UP PAGE -> test case of creating account \n" )
        SignUp_page=page.SignUpPage(self.driver)
        SignUp_page.click_sign_up()
        #when i click on the link it clear my name      
        SignUp_page.insert_ur_name("testing")
        SignUp_page.click_phone_link()      
        SignUp_page.insert_ur_phone("01001729999")
        time.sleep(2) 
       # SignUp_page.choose_day_month_year()
        SignUp_page.click_NEXT()
        if SignUp_page.click_NEXT():
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
        
       
    def test_case_SIGNIN_click_the_button(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case of Sign in button \n" )
        Signin_page=page.SignInPage(self.driver)
        if Signin_page.click_sign_in_button():
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
    
   
    
    def test_case_SIGNIN_check_error_msg(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case of click next without inserting info. \n" )
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(5)
        Signin_page.click_Next_button()
        if Signin_page.check_alert_msg()==SignInLocators.ALERT_MSG_TEXT:
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
     
        
    def test_case_SIGNIN_login_enable(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case of login button is enable withot info. \n" )
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        Signin_page.insert_your_info("testing")
        Signin_page.click_Next_button()
        time.sleep(2)
        if (not Signin_page.is_login_button_enable()):
            failed+=1
            Report.write("FAILED\n\n")
            assert False
        else:
            passed+=1
            Report.write("PASSED\n\n")
            assert True    
    
    
    def test_case_SIGNIN_check_wrong_pass(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case of insert wrong password. \n" )
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        Signin_page.insert_your_info("testing")
        Signin_page.click_Next_button()
        Signin_page.insert_your_password("wrong password")
        time.sleep(2)
        Signin_page.click_login()
        if Signin_page.check_error_msg_of_wrong_password()==SignInLocators.WRONG_PASSWORD_TEXT:
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
    
    
    def test_case_SIGNIN_FORGET_PASSWORD_forget_password(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case of forget password. \n" )
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(2)
        Signin_page.click_forget_password()
        if Signin_page.foregt_ur_password_insert_info("Wrong password"):
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
    
    
    def test_case_SIGNIN_signup(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case Sign up link. \n" )
        Signin_page=page.SignInPage(self.driver)
        SignUp_page=page.SignUpPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(2)
        Signin_page.click_signup()
        if SignUp_page.insert_ur_name("testing"):
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False    
        
      
     
    def test_case_SIGNIN_FORGET_PASSWORD_forget_password(self):
        global testcases
        global passed
        global failed
        testcases+=1
        Report.write("SIGN IN PAGE -> test case of forget password in forget password page. \n" )
        Signin_page=page.SignInPage(self.driver)
        Signin_page.click_sign_in_button()
        time.sleep(2)
        Signin_page.click_signin_with_google()
        if Signin_page.insert_ur_Gmail("testing"):
            passed+=1
            Report.write("PASSED\n\n")
            assert True
        else:
            failed+=1
            Report.write("FAILED\n\n")
            assert False                        
    
       
        
        
    
    
    
    
    
    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        
        
        
if __name__== "__main__":
    unittest.main()
        
        