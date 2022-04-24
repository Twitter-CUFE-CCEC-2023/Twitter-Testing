from selenium.webdriver.common.by import By

class StartingPageLocators(object):
    SIGN_UP_BY_PHONE_OR_EMAIL = (By.LINK_TEXT,"Sign up with a phone number or email")
    SIGN_IN = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/a[1]/div[1]/p[1]")
    SIGN_IN_WITH_APPLE = (By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[2]")
    SIGN_IN_WITH_GOOGLE = ("/html/body/div/div/div[2]")
    
    
class SignInLocators(object):
    INSERT_UR_INFO = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]"
    NEXT_BUTTON = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/p[1]")
    ALERT_MSG ="/html/body/div[1]/div/div/div/div/div[3]"
    SIGN_UP="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/a[1]/span[1]"
    FORGET_PASSWORD="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/a[1]/div[1]/p[1]"
    ALERT_MSG_TEXT="Sorry, we could not find your account."
    INSERT_UR_PASSWORD="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[1]/div[1]/input[1]"
    LOG_IN ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]"
    WRONG_PASSWORD="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]"
    WRONG_PASSWORD_TEXT="Wrong password!"
    INSERT_UR_MAIL_AFTER_FORGET_PASSWORD=""
    SIGNIN_WITH_GOOGLE="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
    INSERT_UR_GMAIL=""
    
class SignUpLocators(object):
    NEXT_BUTTON = (By.XPATH,"//div[@class='css-1dbjc4n r-kemksi r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][normalize-space()='Next']")
    NAME_TEXTBOX =   "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    PHONE_TEXTBOX = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[2]"  #NAME //div[@class='css-1dbjc4n r-1n7yuxj']//div[1]//label[1]//div[1]//div[2]
    MONTH         = "grouped-native-select"
    YEAR            = "SELECTOR_15"
    ERROR_MSG       = "//span[normalize-space()='Please enter a valid phone number.']" #XPATH
    EXPECTED_MSG    = "Please enter a valid phone number."
    WRONG_NAMEX50   ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    NEXT_CREATE_ACCOUNT ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/a[1]/div[1]/p[1]"
    NEXT_PAGE_NEXT ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]"
    EMAIL_TEXTBOX ="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[2]"
    EXPECTED_MSG_EMAIL="Please enter a valid email."
    EMAIL_TEXT="Email"
    EMAIL_TEXT_LOC='div[pseudo="-webkit-input-placeholder"]'
    PHONE_LINK="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/p[1]"
    PHONE_LINK_TEXT="Use phone instead"
    ERROR_MSG_PHONE="" #LOCATIONS
    ERROR_MSG_EMAIL=""
    EMAIL_LINK="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/p[1]"
    EMAIL_LINK_TEXT="Use email instead"
    TEXT_SIGNUP_LOC="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
    NEXT_CREATE_ACCOUNT_CLICK="Next"
class Passwordlocarors(object):
    PASSWORD_TEXTBOX= "password"  #NAME
    FORGET_PASSWORD = "//span[contains(text(),'Forgot password?')]" #XPATH
    LOGIN_BUTTON = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
    FORGET_PASSWORD_TEXT = "Forgot password?"
    
class Settings_Locators(object):
    page_name = 'h2[class="SettingsSection_settings-section-header__uXJhj"]'
    Search_bar = 'input[placeholder="Search settings"]'
    your_account ="/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]"
    Twitter_blue = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]"
    Security_and_Account = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[3]"
    Privacy_and_safety = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[4]"
    notifications = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[5]"
    accessbility = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[6]"
    resources = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[7]"

    your_account_ident ="/html/body/div[1]/div/div/div[2]/div[2]/h2"
    Twitter_blue_ident = " "
    Security_and_Account_ident = " "
    Privacy_and_safety_ident = " "
    notifications_ident = " "
    accessbility_ident = " "
    resources_ident = " "