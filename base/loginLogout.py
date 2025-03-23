from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.locators import dashboard, loginPage

url="https://www.saucedemo.com/"

# username and password
cred=loginPage.creds
uName_std_user=cred['std_user']
uName_locked_out_user=cred['locked_out_user']
uName_problem_user=cred['problem_user']
uName_performance_glitch_user=cred['performance_glitch_user']
uName_error_user=cred['error_user']
uName_visual_user=cred['visual_user']
pWord=cred['pWord']

#xpath and ids for login
xpath=loginPage.xpaths
iD=loginPage.ids
id_uNameField=iD['uNameField']
id_pWordField=iD['pWordField']
id_loginBtn=iD['loginBtn']

#xpaths and ids for logout
xpath=dashboard.xpaths
iD=dashboard.ids
xpath_hamburgerBtn=xpath['hamburgerBtn']
id_logoutLink=iD['logoutLink']


def login(wait,uName=uName_std_user,pWord=pWord):
    uNameField=wait.until(EC.element_to_be_clickable((By.ID,id_uNameField)))
    uNameField.send_keys(uName)
    pWordField=wait.until(EC.element_to_be_clickable((By.ID,id_pWordField)))
    pWordField.send_keys(pWord)
    sleep(1)
    loginBtn=wait.until(EC.element_to_be_clickable((By.ID,id_loginBtn))).click()
    
def logout(wait):
    hamburgerBtn=wait.until(EC.element_to_be_clickable((By.XPATH,xpath_hamburgerBtn))).click()
    logoutLink=wait.until(EC.element_to_be_clickable((By.ID,id_logoutLink))).click()
    