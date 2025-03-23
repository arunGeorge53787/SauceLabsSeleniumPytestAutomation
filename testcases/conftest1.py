import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base import loginLogout

@pytest.fixture(scope="module")
def setup_driver_without_login_and_logout():
    # Correct the path to the actual 'chromedriver' executable
    driver_path = os.path.join(os.path.expanduser("~"), ".wdm", "drivers", "chromedriver", "linux64", "127.0.6533.119", "chromedriver-linux64", "chromedriver")

    # Ensure that 'chromedriver' binary is executable
    os.chmod(driver_path, 0o755)

    # Create an instance of the Chrome WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    wait=WebDriverWait(driver,10)

    url="https://www.saucedemo.com/"
    driver.get(url)

    yield driver,wait
    driver.quit()
