from pages.home_page import HomePage
from utils.initialize_driver import driver_initialize 

def test_login():
    driver = driver_initialize()
    home_page = HomePage(driver)
    home_page.login("usama.pervez@emumba.com", "Usama1234!")
    home_page.click(HomePage.profile_icon)
    home_page_username = home_page.get_text(HomePage.username)
    assert home_page_username == "usama.pervez@emumba.com"
    driver.quit()
    