import pytest
import os
from pytest_html import extras
import re
from time import sleep


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from base import loginLogout
url=loginLogout.url
login=loginLogout.login
logout=loginLogout.logout

service=None

def get_service():
    installed_path = ChromeDriverManager().install()
    word = 'THIRD_PARTY_NOTICES'
    if word in installed_path:
        driver_path = get_driver_path(installed_path, word)
    else:
        driver_path = installed_path
    # print(f"driver path {driver_path}")
    return webdriver.chrome.service.Service(driver_path)

def get_driver_path(installed_path,word):
    match = re.search(rf'\b{word}\b', installed_path)
    dir_path=installed_path[:match.start()] if match else installed_path
    return dir_path+'chromedriver'


@pytest.fixture(scope="module")
def setup_driver_without_login_and_logout():
    global service
    if service is None:
        service=get_service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    driver.get(url)
    yield driver,wait
    driver.quit()


@pytest.fixture(scope="module")
def setup_driver():
    global service
    if service is None:
        service = get_service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    sleep(1)
    login(wait)
    yield driver, wait
    logout(wait)
    driver.quit()



import pytest
import os


@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    #if report.when == "call" and report.failed:
    if report.when == "call":
        ssDir='Screenshots'
        ssFileName = getattr(pytest, "screenshot_name", None)
        #print(f'ssFileName: {ssFileName}')# Get stored path
        ssPath=f'{ssDir}/{ssFileName}'
        screenshot_path=None
        if os.path.abspath(ssPath):
            print(f'os.path.abspath(ssPath): {os.path.abspath(ssPath)}')
            screenshot_path=os.path.abspath(ssPath)
        print(f"screenshot_path: {screenshot_path}")
        if screenshot_path is not None:
            extra = getattr(report, "extras", [])
            extra.append(extras.image(screenshot_path))
            report.extras = extra



