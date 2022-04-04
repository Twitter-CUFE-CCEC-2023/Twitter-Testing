from locator import *
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    
#class insertUrPhone(BasePageElement,SignInLocators):
    #locator= "text"
        
class LoginPage(BasePage):
    def click_sign_in_button(self):
        element = self.driver.find_element(*StartingPageLocators.SIGN_IN)
        element.click()
        
        
    def click_Next_button(self):
        element = self.driver.find_element(*SignInLocators.NEXT_BUTTON)
        element.click()    
    
    def insert_your_info(self , info:str):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,SignInLocators.INSERT_UR_INFO))
                    )
        element.clear()
        element.send_keys(info) 
        
        
    def cheack_ur_error_msg(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,SignInLocators.ALERT_MSG))
                    )
            #element.click()
            print(element.get_attribute("value"))
        except:
            print("halooooo")    
            
class SignUpPage(BasePage):
    def click_sign_up(self):
        element = self.driver.find_element(*StartingPageLocators.SIGN_UP_BY_PHONE_OR_EMAIL)
        element.click()
        
    def insert_ur_name(self, name:str):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,SignUpLocators.NAME_TEXTBOX))
                    )
        element.clear()
        element.send_keys(name)
         
    def insert_ur_phone(self, phone:str):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,SignUpLocators.PHONE_TEXTBOX))
                    )
        element.clear()
        element.send_keys(phone)
            
    def check_wrong_msg(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,SignUpLocators.ERROR_MSG))
                    )
        msg=element.text
        return msg
    def cheack_ur_name_size(self):
            element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME,SignUpLocators.NAME_TEXTBOX))
                    )
            check=0
            check=len(element.get_attribute("value"))
            if check>50:
                return False
            else:
                 return  True   
    def choose_day_month_year(self):
        ''''
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(  (By.CLASS_NAME,SignUpLocators.MONTH))
                    )
        element.click()
        '''
        vv = self.driver.find_element((By.CLASS_NAME,"r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-1nao33i r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"))
        vv.click()
        print("hallo")  
        
    def click_NEXT(self):
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,SignUpLocators.NEXT_CREATE_ACCOUNT))
                    )
            element.click() 
            '''
            try :
                element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,SignUpLocators.NEXT_PAGE_NEXT))
                    )
                element.click()
                return True
            except:
                return False
            '''       
          
        
              
class loginbyGoogle(BasePage):
     def click_sign_in_with_Gmail(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,StartingPageLocators.SIGN_IN_WITH_APPLE))
                    )
        element.click()
        