from data.config import settings 


class WebApp:

    def __init__(self, driver):
        self.driver = driver

    
    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
                
