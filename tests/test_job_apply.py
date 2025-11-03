from pages.job_apply import JobApply
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.initialize_driver import driver_initialize 

def test_job_apply():
    driver = driver_initialize()
    homePage = HomePage(driver)
    homePage.login("usama.pervez@emumba.com", "Usama1234!")
    searchPage = SearchPage(driver)
    searchPage.get_search_results()
    job_apply = JobApply(driver)
    job_apply.apply_to_first_job()
    assert job_apply.is_upload_box_displayed() == True, "Application submission failed"
    driver.quit()