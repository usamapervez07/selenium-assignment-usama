from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    search_field = (By.XPATH, "//input[@data-gtm-category = 'keyword-dropdown']")
    location_field = (By.XPATH, "//input[@data-gtm-category = 'location-dropdown']")
    search_button = (By.XPATH, "//button[@type = 'submit']") 
    search_results = (By.XPATH, "(//div[contains(@class, 'job-search-results')])[3]//efc-job-card")

    def get_search_results(self):
        self.click(self.search_field)
        self.enter_text(self.search_field, "QA")
        self.click(self.location_field)
        self.enter_text(self.location_field, "London")
        self.click(self.search_button)