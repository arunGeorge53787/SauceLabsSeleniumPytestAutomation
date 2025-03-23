import pytest
import os
from pytest_html import extras
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from base import loginLogout

url = loginLogout.url
login = loginLogout.login
logout = loginLogout.logout

service = None


def get_service():
    """Install and return ChromeDriver service"""
    installed_path = ChromeDriverManager().install()
    word = 'THIRD_PARTY_NOTICES'

    if word in installed_path:
        driver_path = get_driver_path(installed_path, word)
    else:
        driver_path = installed_path

    return Service(driver_path)


def get_driver_path(installed_path, word):
    """Extract correct ChromeDriver path from installed location"""
    match = re.search(rf'\b{word}\b', installed_path)
    dir_path = installed_path[:match.start()] if match else installed_path
    return os.path.join(dir_path, 'chromedriver')


@pytest.fixture(scope="module")
def setup_driver_without_login_and_logout():
    """Fixture to set up a WebDriver instance without login/logout"""
    global service
    if service is None:
        service = get_service()

    options = Options()
    #options.add_argument("--headless")  # Run in headless mode for CI/CD
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    yield driver, wait
    driver.quit()


@pytest.fixture(scope="module")
def setup_driver():
    """Fixture to set up a WebDriver instance with login/logout"""
    global service
    if service is None:
        service = get_service()

    options = Options()
    #options.add_argument("--headless")  # Required for GitHub Actions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    sleep(1)

    login(wait)
    yield driver, wait
    logout(wait)

    driver.quit()
