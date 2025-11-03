from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def driver_initialize(grid_url="http://localhost:4444/wd/hub", browser= "chrome"):
        if browser == "chrome":
            options = Options()
            driver = webdriver.Remote(
                command_executor=grid_url,
                options=options
            )
        elif browser == "firefox":
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            options = FirefoxOptions()
            driver = webdriver.Remote(
                command_executor=grid_url,
                options=options
            )
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.get("https://www.efinancialcareers.com/")
        driver.implicitly_wait(10)
        return driver