from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class JobApply(BasePage):
    apply_now = (By.XPATH, "(//a[contains(text(), 'Apply now')])[1]")
    first_name_field = (By.XPATH, "//input[@id='firstname']")
    last_name_field = (By.XPATH, "//input[@id='lastname']")
    upload_resume_button = (By.XPATH, "//button[.//span[contains(text(), 'Upload Resume')]]")
    upload_box = (By.XPATH, "//div[contains(text(), 'Select Files to Upload')]")

    def apply_to_first_job(self):
        self.click(self.apply_now)
        self.click(self.apply_now)
        self.enter_text(self.first_name_field, "Usama")
        self.enter_text(self.last_name_field, "Pervez")
        self.click(self.upload_resume_button)

    def is_upload_box_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.upload_box))
        return True
        
