from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Prod_Img_Name_Price_AddToCartBtn:
    def __init__(self, wait):
        self.wait = wait

    def locate_elt_presence(self,xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def locate_elts_presence_class(self,className):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, className)))

    def locate_Btn(self,xpath):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def locate_elt_Visibility(self,xpath):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

