
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_functions

class example:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)
        self.global_function = global_functions(self.driver)

    def user(self,texto):
        try:
            self.global_function.text("id","email",texto)
            return True
        except TimeoutException as e:
            raise e
        
    def validador(self):
        try:
            self.global_function.element_present("xpath","//img[@alt='Facebosok']")
            return True
        except TimeoutException as e:
            raise e