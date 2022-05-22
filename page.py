from pickle import TRUE
from numpy import true_divide
from locator import *
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver_manger.chrome import ChromeDriverManger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    
#class insertUrPhone(BasePageElement,SignInLocators):
    #locator= "text"
        
class SignInPage(BasePage):
    def click_sign_in_button(self):
        try:
            element = self.driver.find_element(*StartingPageLocators.SIGN_IN)
            element.click()
            return True
        except:
            return False
                
        
        
    def click_Next_button(self):
        try:
            element = self.driver.find_element(*SignInLocators.NEXT_BUTTON)
            element.click()
            return True
        except:
            return False        
    
    def check_alert_msg(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.ALERT_MSG))
                    )
            return element.text
        except:
            return False
        
        
    def insert_your_info(self , info:str):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.INSERT_UR_INFO))
                    )
            element.clear()
            element.send_keys(info)
        except:
            return False     
    def insert_your_password(self , info:str):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.INSERT_UR_PASSWORD))
                    )
            element.clear()
            element.send_keys(info)
        except:
            return False         
    
    def is_login_button_enable(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.LOG_IN))
                    )
            print("hallo")
            return element.is_enabled()
        except:
            return "False"
    def click_login(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.LOG_IN))
                    )
            element.click()
            return True
        except:
            return False
    def check_error_msg_of_wrong_password(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.WRONG_PASSWORD))
                    )
            return element.text
        except:
            return False
    def click_forget_password(self):
        
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.FORGET_PASSWORD))
                    )
            element.click()
            return True
        except:
            return False  
    def click_forget_password_1(self):
            
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.FORGET_PASSWORD_2))
                    )
            element.click()
            return True
        except:
            return False     
    def click_forget_password_in(self):
        
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.FORGET_PASSWORD_1))
                    )
            element.click()
            return True
        except:
            return False               
    def foregt_ur_password_insert_info(self , info:str):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.INSERT_UR_MAIL_AFTER_FORGET_PASSWORD))
                    )
            element.clear()
            element.send_keys(info)
            return True
        except:
            return False   
    def click_signup(self):
        
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.SIGN_UP))
                    )
            element.click()
            return True
        except:
            return False         
    def click_signin_with_google(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.SIGNIN_WITH_GOOGLE))
                    )
            element.click() 
        except:
            return False 
    def insert_ur_Gmail(self,Email:str):
        
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.INSERT_UR_GMAIL))
                    )
            element.clear()
            element.send_keys(Email)
            return True
        except:
            return False  
        
    def is_search_button_enable(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.SEARCH_BUTTON))
                    )
            return element.is_enabled()
        except:
            return "False" 
    def click_search_button(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.SEARCH_BUTTON_1))
                    )
            element.click()
            return
        except:
            print("i am")
            return "False"  
    def check_alert_msg_of_forget_password(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.ALERT_MSG_FORGET_PASSWORD))
                    )
            return element.text
        except:
            return False       
    def insert_ver_code(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignInLocators.VER_CODE))
                    )
            element.clear()
            element.send_keys("293922")
            return True
        except:
            return False
                    
class SignUpPage(BasePage):
    def insert_ur_email(self,Email:str):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID,SignUpLocators.EMAIL_TEXTBOX))
                    )
        element.clear()
        element.send_keys(Email)
    def insert_ur_username(self,username:str):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID,SignUpLocators.USERNAME_TEXTBOX))
                    )
        element.clear()
        element.send_keys(username)    
    def click_NEXT_in_next_page(self):
            try:
                element = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.NEXT_PAGE_NEXT))
                    )
                element.click() 
                return True     
            except:
                return False         
    def select_gender(self,gender):
            try:
                element = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.GENDER))
                    )
                
                drop=Select(element)
                drop.select_by_value(gender)
                return True     
            except:
                return False        
    def Check_year(self,year):
        try:
                years = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.YEAR))
                    )
              
                years=Select(years)
                try:
                    years.select_by_value(year)
                    return True
                except:
                    return False
                   
        except:
                return False       
    def select_age(self,day,month,year):
            try:
                mon = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.MONTH))
                    )
                dia = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.DAY))
                    )
                
                years = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.YEAR))
                    )
                dia=Select(dia)
                dia.select_by_value(day)
                mon=Select(mon)
                mon.select_by_value(month)
                years=Select(years)
                years.select_by_value(year)
                
                return True     
            except:
                return False           
    def click_sign_up(self):
        try:
            element = self.driver.find_element(*StartingPageLocators.SIGN_UP_BY_PHONE_OR_EMAIL)
            element.click()
            return True
        except:
            return False
        
    def insert_ur_name(self, name:str):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.NAME_TEXTBOX))
                    )
            element.clear()
            element.send_keys(name)
            return True
        except:
            return False   
    def click_phone_link(self):
            try:
                element = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH,SignUpLocators.PHONE_LINK))
                    )
                element.click()      
            except:
                return False         
    def check_phone_link(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.PHONE_LINK))
                    )
            msg=element.text  
            #print("her",msg)
            return msg
        except:
            return False     
    def insert_ur_phone(self, phone:str): 
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID,SignUpLocators.PHONE_TEXTBOX))
                    )
        element.clear()
        element.send_keys(phone)
    def check_wrong_msg_email(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.ERROR_MSG_EMAIL))
                    )
            msg=element.text
            return msg
        except:
            return False        
    def check_wrong_msg_phone(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.ERROR_MSG_PHONE))
                    )
            msg=element.text
            return msg
        except:
            return False
    def check_Email_link(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.EMAIL_LINK))
                    )
            msg=element.text
            print(msg)  
            return msg
        except:
            return False
        
    def cheack_ur_name_size(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.NAME_TEXTBOX))
                    )
            check=0
            check=len(element.get_attribute("value"))
            if check>50:
                return False
            else:
                 return  True
        except:
            return False        
    def choose_day_month_year(self,Month:str,Day:int,Year:int):
        ''''
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(  (By.CLASS_NAME,SignUpLocators.MONTH))
                    )
        element.click()
        '''
        vv = self.driver.find_element((By.CLASS_NAME,"r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-1nao33i r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"))
        vv.click()
        print("hallo")  
    def check_text_in_signup_page(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.TEXT_SIGNUP_LOC))
                    )
            msg=element.text
            print(msg)
            return msg
        except:
            return False
             
    def click_NEXT(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.NEXT_CREATE_ACCOUNT))
                    )
            element.click()
            return True 
        except:
            return False    
    def is_NEXT_enable(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.NEXT_CREATE_ACCOUNT))
                    )
        print("the button",element.is_enabled())
        return element.is_enabled()
   
            
        
              
class loginbyGoogle(BasePage):
    def click_sign_in_with_Gmail(self):
        try:
            
            element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,StartingPageLocators.SIGN_IN_WITH_GOOGLE))
                    )
            element.click()
            return True
        except:
            return False    
    
    def insert_ur_gamil(self,email):
        try:
            element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,StartingPageLocators.SIGN_IN_WITH_GOOGLE))
                    )
            element.send_keys(email)
            return True
        except:
            return False    

class enteryourpassword(BasePage):
    def enter_your_password(self,paswword:str):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,Passwordlocarors.PASSWORD_TEXTBOX))
                    )
        element.clear()
        element.send_keys(paswword)
        
    def is_login_enable(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,Passwordlocarors.LOGIN_BUTTON))
                    )
        return(element.is_enabled())
            
    def forget_password(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,Passwordlocarors.FORGET_PASSWORD))
                    )
        return element.text           
    def click_login(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,Passwordlocarors.LOGIN_BUTTON))
                    )
        element.click()