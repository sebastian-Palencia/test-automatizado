
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions
import time
class login:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)
        self.global_function = global_functions(self.driver)

    def user(self,username):
        try:
            self.global_function.text("xpath","//input[@placeholder='Username']",username)
            return True
        except TimeoutException as e:
            raise e
        
    def password(self,password):
        try:
            self.global_function.text("xpath","//input[@placeholder='Password']",password)
            return True
        except TimeoutException as e:
            raise e
        
    def loginButton(self):
        try:
            self.global_function.click("xpath","//button[normalize-space()='Login']")
            return True
        except TimeoutException as e:
            raise e


    def validaciondeportaldeorange(self):
        try:
            time.sleep(10)
            self.global_function.element_present("xpath","//div[@class='orangehrm-attendance-card-profile-image']//img[@alt='profile picture']")
            return True
        except TimeoutException as e:
            raise e
        
    def pimmenubutton(self):
        try:
            self.global_function.click("xpath","//span[normalize-space()='PIM']")
            return True
        except TimeoutException as e:
            raise e
    
    def addemployed(self):
        try:
            self.global_function.click("xpath","//button[normalize-space()='Add']")
            return True
        except TimeoutException as e:
            raise e
        
    def create_login_details_button(self):
        try:
            self.global_function.click("xpath","//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
            return True
        except TimeoutException as e:
            raise e
        
    def inputform(self,texto,locator):
        try:
            self.global_function.text("xpath",locator,texto)
            return True
        except TimeoutException as e:
            raise e
        
    def clicksavebutton(self):
        try:
            self.global_function.click("xpath","//button[normalize-space()='Save']")
            return True
        except TimeoutException as e:
            raise e