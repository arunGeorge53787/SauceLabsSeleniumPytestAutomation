from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys


class Get_Elts:
    def __init__(self, wait):
        self.wait = wait

    def presOfEltByXpath(self, xpath):
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            return None
    def presOfAllEltsByClass(self, className):
        try:
            return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, className)))
        except TimeoutException:
            return None
    def visibilityOfEltByXpath(self, xpath):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            return None
    def clickabilityOfEltByXpath(self, xpath):
        try:
            return self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            return None
    def presOfEltById(self, Id):
        try:
            return self.wait.until(EC.presence_of_element_located((By.ID, Id)))
        except TimeoutException:
            return None

    def presOfEltByTagName(self, tagName):
        try:
            return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, tagName)))
        except TimeoutException:
            return None

    def clickabilityOfEltById(self, Id):
        try:
            return self.wait.until(EC.element_to_be_clickable((By.ID, Id)))
        except TimeoutException:
            return None
