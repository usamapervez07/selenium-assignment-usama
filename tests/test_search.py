from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.initialize_driver import driver_initialize

def test_search():
    driver = driver_initialize()
    home_page = HomePage(driver)
    driver.fullscreen_window()
    home_page.login("usama.pervez@emumba.com", "Usama1234!")
    search_page = SearchPage(driver)
    search_page.get_search_results()
    assert search_page.search_results is not None, "No search results found"
    driver.quit()