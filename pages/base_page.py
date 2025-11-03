from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.get("https://www.efinancialcareers.com/")
        self.wait = WebDriverWait(driver, timeout=10)


    def click(self, locator):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        time.sleep(15)

    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
