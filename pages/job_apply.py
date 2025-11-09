from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class JobApply(BasePage):
    apply_now = (By.XPATH, "(//a[contains(text(), 'Apply now')])[1]")
    first_name_field = (By.XPATH, "//input[@id='firstname']")
    last_name_field = (By.XPATH, "//input[@id='lastname']")
    select_resume_dropdown = (By.XPATH, "//button[.//span[contains(text(), 'Select a Resume')]]")
    upload_resume_button = (By.XPATH, "//div[contains(@class, 'add-file')]")    
    upload_box = (By.XPATH, "//div[contains(text(), 'Select Files to Upload')]")
    submit_button = (By.XPATH, "//button[@data-gtm-trackable='submit-job-application-become-searchable']")

    def apply_to_first_job(self):
        self.click(self.apply_now)
        self.click(self.apply_now)
        self.enter_text(self.first_name_field, "Usama")
        self.enter_text(self.last_name_field, "Pervez")

    def is_submit_application_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button))
        return True
        
