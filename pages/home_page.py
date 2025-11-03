from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    sign_in_button = (By.XPATH, "//button[@data-gtm-trackable='login-register']")
    email_text_field = (By.XPATH, "//input[@name='email']")
    password_text_field = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//button[text()='Submit']")
    continue_button= (By.XPATH, "//button[text()='Continue']")
    google_sign_in = (By.XPATH, "//efc-icon[contains(@class, 'close-button')]")
    profile_icon = (By.XPATH, "//efc-icon[@icon='profile']")
    username = (By.XPATH, "//div[@class='dropdown-avatar-user-details']/span")

    def login(self, email, password):
        self.click(self.google_sign_in)
        self.click(self.sign_in_button)
        self.click(self.email_text_field)
        self.enter_text(self.email_text_field, email)
        self.click(self.continue_button)
        self.click(self.password_text_field)
        self.enter_text(self.password_text_field, password)
        self.click(self.submit_button)