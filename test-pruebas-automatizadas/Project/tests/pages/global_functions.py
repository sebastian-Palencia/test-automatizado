import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from colorama import  Fore
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



class global_functions:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)
        
    def _wait_for_spinner_to_disappear(self):
        try:
            WebDriverWait(self.driver, 60).until(
                EC.invisibility_of_element_located((By.ID, "spinner_background"))
            )
        except TimeoutException as e:
            raise TimeoutException("Timeout waiting for spinner to disappear") from e


    def time(self, seconds):
        time.sleep(seconds)
        return seconds
        
    def select_element_xpath(self, element, timeout=10):
        try:
            element_xpath = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
            element_xpath = self.driver.find_element(By.XPATH, element)
            return element_xpath
        except TimeoutException as e:
            raise e

    

    def select_element_id(self, element, timeout=5):
        try:
            element_id = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, element)))

            element_id = self.driver.find_element(By.ID, element)
            return element_id      
        except TimeoutException as e:
            raise e

    def select_element_css(self, element, timeout=5):
        try:
            element_css = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            element_css = self.driver.find_element(By.CSS_SELECTOR, element)
            return element_css
        except TimeoutException as e:
            raise e

    def text(self, selector_type, selector_name, input_text, timeout=10):
        try:
            selectors = {
                "xpath": self.select_element_xpath,
                "id": self.select_element_id
            }

            selector_method = selectors.get(selector_type)
            if selector_method:
                try:
                    element = selector_method(selector_name, timeout)
                    if element:
                        element.clear()
                        time.sleep(1)
                        element.send_keys(input_text)
                    else:
                        raise NoSuchElementException(f"Could not find element {selector_name} ({selector_type})")
                except TimeoutException as ex:
                    raise TimeoutException(f"Timed out waiting for element {selector_name} ({selector_type}) to be present") from ex
                except NoSuchElementException as ex:
                    raise NoSuchElementException(f"Could not find element {selector_name} ({selector_type}): {str(ex)}") from ex
            else:
                raise ValueError(f"Invalid selector type: {selector_type}")
        except TimeoutException as e:
            raise e

    def click(self, selector_type, selector_value, timeout=30):
        try:
            by_types = {
                "xpath": By.XPATH,
                "id": By.ID,
                "css": By.CSS_SELECTOR
            }

            if selector_type not in by_types:
                print(Fore.RED + f"----- Tipo de selector inválido: {selector_type}" + Fore.RESET)
                return

            by = by_types[selector_type]
            # Esperar a que el elemento sea clickeable
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable((by, selector_value)))

            # Hacer clic en el elemento
            element.click()
            print(Fore.GREEN + f"✔ Elemento clickeado correctamente: {selector_value}" + Fore.RESET)

        except (TimeoutException, NoSuchElementException) as ex:
            print(Fore.RED + f"❌ No se pudo encontrar o hacer clic en el elemento '{selector_value}' usando '{selector_type}': {str(ex)}" + Fore.RESET)
            raise
        except Exception as ex:
            print(Fore.RED + f"❌ Error inesperado al hacer clic en el elemento '{selector_value}': {str(ex)}" + Fore.RESET)
            raise



    def select(self, selector_type, selector_name, select_type, select_value, time_wait=4):
        try:
            selectors = {
                "xpath": self.select_element_xpath,
                "id": self.select_element_id
            }

            select_method = selectors.get(selector_type)
            if select_method:
                element = select_method(selector_name, time_wait)
                select = Select(element)
                if select_type == "text":
                    select.select_by_visible_text(select_value)
                elif select_type == "value":
                    select.select_by_value(select_value)
                elif select_type == "index":
                    select.select_by_index(select_value)
                else:
                    print(Fore.RED + "-----Invalid select type: {select_type}" + Fore.RESET)
                    return
            else:
                print(Fore.RED + f"-----Invalid selector type: {selector_type}" + Fore.RESET)
        except TimeoutException as e:
            raise e

    def upload_file(self, selector_type, selector_name, file_path, wait_time):
        try:
            element = self.select_element_xpath(selector_name)
            element.send_keys(file_path)
            time.sleep(wait_time)
        except TimeoutException as e:
            raise e

    def wait_for_element(self, locator, selector, timeout=10):
        try:
            if locator == "id":
                try:
                    element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, selector)))
                    element = self.driver.execute_script("arguments[0].scrollIntoView()", element)
                    element = self.driver.find_element(By.ID, selector)
                    time.sleep(timeout)
                except TimeoutException as ex:
                    raise ex

            elif locator == "xpath":
                try:
                    element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, selector)))
                    element = self.driver.execute_script("arguments[0].scrollIntoView()", element)
                    element = self.driver.find_element(By.XPATH, selector)
                    time.sleep(timeout)
                except TimeoutException as ex:
                    raise ex
        except TimeoutException as e:
            raise e

    def click_checkboxes_by_xpath(self, wait_time, *xpaths):
        try:
            for xpath in xpaths:
                checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                checkbox = self.driver.execute_script("arguments[0].scrollIntoView()", checkbox)
                checkbox.click()
                time.sleep(wait_time)
        except TimeoutException as e:
            raise e


    def element_present(self, locator_type, selector, timeout=13):
        try:
            locator = getattr(By, locator_type.upper())
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, selector)))
            element = self.driver.execute_script("arguments[0].scrollIntoView()", element)
            return "Exists"
        except TimeoutException as e:
            raise e

        
    def find_element(self, selector_type, selector_value, timeout=10):
        try:
            selectors = {
                "xpath": By.XPATH,
                "id": By.ID,
                "css": By.CSS_SELECTOR
            }
            by = selectors.get(selector_type.lower())
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, selector_value)))
            self.driver.execute_script("arguments[0].scrollIntoView()", element)
            return element
        except TimeoutException as e:
            raise e

        
    def hover_element(self, selector_type, selector_value, timeout=10):
        try:
            element = self.find_element(selector_type, selector_value, timeout)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except TimeoutException as e:
            raise e

        
    def hover_and_validate_text(self, hover_selector_type, hover_selector_value, text_selector_type, text_selector_value, expected_text, timeout=10):
        try:
            self.hover_element(hover_selector_type, hover_selector_value, timeout)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, text_selector_value))
            )
    
            text_element = self.find_element(text_selector_type, text_selector_value, timeout)
            actual_text = text_element.text.strip()
            if actual_text == expected_text:
                print(f"-----Text '{expected_text}' is visible after hover.")
            else:
                raise AssertionError(f"Expected text '{expected_text}', but found '{actual_text}'.")
        except TimeoutException as e:
            raise e

        
    def hover_and_validate_element(self, hover_selector_type, hover_selector_value, text_selector_type, text_selector_value, expected_text, timeout=10):
        try:
            self.hover_element(hover_selector_type, hover_selector_value, timeout)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, text_selector_value))
            )
            text_element = self.find_element(text_selector_type, text_selector_value, timeout)
            actual_text = text_element.text.strip()
            if actual_text == expected_text:
                print(f"-----Text '{expected_text}' is visible after hover.")
            else:
                raise AssertionError(f"Expected text '{expected_text}', but found '{actual_text}'.")
        except TimeoutException as e:
            raise e
