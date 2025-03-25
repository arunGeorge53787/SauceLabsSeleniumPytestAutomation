#import time
import pytest
from base import loginLogout, saveScreenShots
from selenium.common.exceptions import TimeoutException
from data.locators import loginPage, dashboard
from testcases import getElts

login=loginLogout.login
logout=loginLogout.logout
eltLocator=getElts.Get_Elts
saveSS=saveScreenShots.saveScreenshot

# xpaths and ids of elements in login page
xpath=loginPage.xpaths
iD=loginPage.ids
xpath_logo=xpath['logo']
id_uNameField=iD['uNameField']
id_pWordField=iD['pWordField']
id_loginBtn=iD['loginBtn']
xpath_errorCloseBtn=xpath['errorCloseBtn']

#credentials
creds=loginPage.creds
uName_std_user=creds['std_user']
uName_locked_out_user=creds['locked_out_user']
uName_problem_user=creds['problem_user']
uName_performance_glitch_user=creds['performance_glitch_user']
uName_error_user=creds['error_user']
uName_visual_user=creds['visual_user']
pWord=creds['pWord']

#warnings for invalid login attempts
tagName=loginPage.tagNames
tag_warningLabel=tagName['warningLabel']
text=loginPage.warningTexts
warningText_noUserNameNoPassword=text['noUserNameNoPassword']
warningText_noPassword=text['noPassword']
warningText_noUsername=text['noUsername']
warningText_incorrectUsername=text['incorrectUsername']
warningText_incorrectPassword=text['incorrectPassword']
warningText_lockedOutUser=text['lockedOutUser']

#xpath dashboard elements
xpath=dashboard.xpaths
xpath_title=xpath['title']

#@pytest.mark.skip
class Test_loginPageElementsAndLoginFunctionality:
    driver=None
    wait=None
    presOfEltByXpath=None
    presOfAllEltsByClass=None
    visibilityOfEltByXpath=None
    clickabilityOfEltByXpath=None
    presOfEltById=None
    presOfEltByTagName=None
    clickabilityOfEltById=None

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request, setup_driver_without_login_and_logout):
        request.cls.driver, request.cls.wait = setup_driver_without_login_and_logout
        request.cls.locator = eltLocator(request.cls.wait)
        locatorClass = request.cls.locator
        request.cls.presOfEltByXpath = locatorClass.presOfEltByXpath
        request.cls.presOfAllEltsByClass = locatorClass.presOfAllEltsByClass
        request.cls.visibilityOfEltByXpath = locatorClass.visibilityOfEltByXpath
        request.cls.clickabilityOfEltByXpath = locatorClass.clickabilityOfEltByXpath
        request.cls.presOfEltById = locatorClass.presOfEltById
        request.cls.presOfEltByTagName=locatorClass.presOfEltByTagName
        request.cls.clickabilityOfEltById=locatorClass.clickabilityOfEltById
    
    def test_logo_in_login_page(self):
        title='verify that login page displays company logo'
        #pytest.title = title
        logo=self.visibilityOfEltByXpath(xpath_logo)
        if logo is not None:
            try:
                assert logo.is_displayed()==True
                ssName = saveSS(self.driver, 'test_logo_in_login_page')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_logo_in_login_page')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_logo_in_login_page')
            pytest.screenshot_name = ssName
            pytest.fail("logo not found")
    
    def test_uNameField(self):
        title='verify that the login page has a username field'
        #pytest.title = title
        uNameField=self.presOfEltById(id_uNameField)
        if uNameField is not None:
            try:
                assert uNameField.is_displayed() and uNameField.is_enabled() == True
                ssName = saveSS(self.driver, 'test_uNameField')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_uNameField')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_uNameField')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
    def test_uNameFieldPlaceholder(self):
        title='verify that the username field has the placeholder username'
        #pytest.title = title
        uNameField=self.presOfEltById(id_uNameField)
        if uNameField is not None:
            try:
                assert uNameField.get_attribute("placeholder") == 'Username'
                ssName = saveSS(self.driver, 'test_uNameFieldPlaceholder')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_uNameFieldPlaceholder')
                pytest.screenshot_name = ssName
        else:
            ssName = saveSS(self.driver, 'test_uNameFieldPlaceholder')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
    
    def test_pWordField(self):
        title='verify that the login page has a password field'
        #pytest.title = title
        pWordField=self.presOfEltById(id_pWordField)
        if pWordField is not None:
            try:
                assert pWordField.is_displayed() and pWordField.is_enabled() == True
                ssName = saveSS(self.driver, 'test_pWordField')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_pWordField')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_pWordField')
            pytest.screenshot_name = ssName
            pytest.fail("pWordField not found")
        
    def test_pWordFieldPlaceholder(self):
        title='verify that the password field has the placeholder password'
        #pytest.title = title
        pWordField=self.presOfEltById(id_pWordField)
        if pWordField is not None:
            try:
                assert pWordField.get_attribute("placeholder") == 'Password'
                ssName = saveSS(self.driver, 'test_pWordFieldPlaceholder')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_pWordFieldPlaceholder')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_pWordFieldPlaceholder')
            pytest.screenshot_name = ssName
            pytest.fail("pWordField not found")
        
    def test_presenceOfLoginBtn(self):
        title='verify that the login page has a login button'
        #pytest.title = title
        loginBtn=self.presOfEltById(id_loginBtn)
        if loginBtn is not None:
            try:
                assert loginBtn.is_displayed() and loginBtn.is_enabled() == True
                ssName = saveSS(self.driver, 'test_presenceOfLoginBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_presenceOfLoginBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_presenceOfLoginBtn')
            pytest.screenshot_name = ssName
            pytest.fail("loginBtn not found")
    
    def test_nameOfLoginBtn(self):
        title='verify that the login button has the name Login'
        #pytest.title = title
        loginBtn=self.presOfEltById(id_loginBtn)
        if loginBtn is not None:
            try:
                assert loginBtn.get_attribute("value")=='Login'
                ssName = saveSS(self.driver, 'test_nameOfLoginBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_nameOfLoginBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_nameOfLoginBtn')
            pytest.screenshot_name = ssName
            pytest.fail("loginBtn not found")

    def test_loginWithoutCredentials(self):
        title='verify that the user is not logged in without any values in the username and password fields and user is provided with a warning that username is required'
        #pytest.title = title
        loginBtn = self.presOfEltById(id_loginBtn)
        if loginBtn is not None:
            loginBtn.click()
            warningMsg=""
            try:
                warningMsg=self.presOfEltByTagName(tag_warningLabel).text
            except TimeoutException:
                pageTitle=self.visibilityOfEltByXpath(xpath_title)
                if pageTitle.is_displayed():
                    ssName = saveSS(self.driver, 'test_loginWithoutCredentials')
                    pytest.screenshot_name = ssName
                    logout(self.wait)
                    pytest.fail("login success")
            try:
                assert warningMsg==warningText_noUserNameNoPassword
                ssName = saveSS(self.driver, 'test_loginWithoutCredentials')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_loginWithoutCredentials')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_loginWithoutCredentials')
            pytest.screenshot_name = ssName
            pytest.fail("loginBtn not found")
    
    def test_test_loginWithoutUsername(self):
        title='verify that the user is unable to login without a username'
        #pytest.title = title
        pWordField=self.presOfEltById(id_pWordField)
        if pWordField is not None:
            pWordField.send_keys(pWord)
            loginBtn=self.clickabilityOfEltById(id_loginBtn)
            if loginBtn is not None:
                loginBtn.click()
                warningMsg=""
                try:
                    warningMsg=self.presOfEltByTagName(tag_warningLabel).text
                except TimeoutException:
                    pageTitle=self.visibilityOfEltByXpath(xpath_title)
                    if pageTitle.is_displayed():
                        ssName = saveSS(self.driver, 'test_test_loginWithoutUsername')
                        pytest.screenshot_name = ssName
                        logout(self.wait)
                        pytest.fail("login success")
                try:
                    assert warningMsg==warningText_noUsername
                    ssName = saveSS(self.driver, 'test_test_loginWithoutUsername')
                    pytest.screenshot_name = ssName
                except AssertionError as e:
                    ssName = saveSS(self.driver, 'test_test_loginWithoutUsername')
                    pytest.screenshot_name = ssName
                    raise
            else:
                ssName = saveSS(self.driver, 'test_test_loginWithoutUsername')
                pytest.screenshot_name = ssName
                pytest.fail("loginBtn not found")
        
    def test_loginWithoutPassword(self):
        title='verify that the user is unable to login without password'
        #pytest.title = title
        self.driver.refresh()
        uNameField=self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys(uName_std_user)
            loginBtn=self.clickabilityOfEltById(id_loginBtn)
            if loginBtn is not None:
                loginBtn.click()
                warningMsg=""
                try:
                    warningMsg=self.presOfEltByTagName(tag_warningLabel).text
                except TimeoutException:
                    pageTitle=self.visibilityOfEltByXpath(xpath_title)
                    if pageTitle.is_displayed():
                        ssName = saveSS(self.driver, 'test_loginWithoutPassword')
                        pytest.screenshot_name = ssName
                        logout(self.wait)
                        pytest.fail("login success")
                try:
                    assert warningMsg==warningText_noPassword
                    ssName = saveSS(self.driver, 'test_loginWithoutPassword')
                    pytest.screenshot_name = ssName
                except AssertionError as e:
                    ssName = saveSS(self.driver, 'test_loginWithoutPassword')
                    pytest.screenshot_name = ssName
                    raise
            else:
                ssName = saveSS(self.driver, 'test_loginWithoutPassword')
                pytest.screenshot_name = ssName
                pytest.fail("loginBtn not found")
        else:
            ssName = saveSS(self.driver, 'test_loginWithoutPassword')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
    def test_loginWithInvalidUsername(self):
        title='verify that the user is unable to login with invalid username'
        #pytest.title = title
        self.driver.refresh()
        uNameField=self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys("abc")
            pWordField=self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys(pWord)
                loginBtn=self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    warningMsg=""
                    try:
                        warningMsg=self.presOfEltByTagName(tag_warningLabel).text
                    except TimeoutException:
                        pageTitle=self.presOfEltByXpath(xpath_title)
                        if pageTitle.is_displayed():
                            ssName = saveSS(self.driver, 'test_loginWithInvalidUsername')
                            pytest.screenshot_name = ssName
                            logout(self.wait)
                            pytest.fail("login success")
                    assert warningMsg==warningText_incorrectUsername
                else:
                    pytest.fail("loginBtn not found")
            else:
                pytest.fail("pWordField not found")
        else:
            pytest.fail("uNameField not found")
       
    def test_loginWithInvalidPassword(self):
        title='verify that the user is unable to login with invalid password'
        #pytest.title = title
        self.driver.refresh()
        uNameField = self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys(uName_std_user)
            pWordField = self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys("abc")
                loginBtn = self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    warningMsg=""
                    try:
                        warningMsg = self.presOfEltByTagName(tag_warningLabel).text
                    except TimeoutException:
                        pageTitle = self.presOfEltByXpath(xpath_title)
                        if pageTitle.is_displayed():
                            ssName = saveSS(self.driver, 'test_loginWithInvalidPassword')
                            pytest.screenshot_name = ssName
                            logout(self.wait)
                            pytest.fail("login success")
                    try:
                        assert warningMsg==warningText_incorrectPassword
                        ssName = saveSS(self.driver, 'test_loginWithInvalidPassword')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_loginWithInvalidPassword')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_loginWithInvalidPassword')
                    pytest.screenshot_name = ssName
                    pytest.fail("loginBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_loginWithInvalidPassword')
                pytest.screenshot_name = ssName
                pytest.fail("pWordField not found")
        else:
            ssName = saveSS(self.driver, 'test_loginWithInvalidPassword')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
    def test_loginWithInvalidUsernameAndPassword(self):
        title='verify that the user is unable to login with invalid username and password'
        #pytest.title = title
        self.driver.refresh()
        uNameField = self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys("uName_std_user")
            pWordField = self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys("abc")
                loginBtn = self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    warningMsg=""
                    try:
                        warningMsg = self.presOfEltByTagName(tag_warningLabel).text
                    except TimeoutException:
                        pageTitle = self.presOfEltByXpath(xpath_title)
                        if pageTitle.is_displayed():
                            ssName = saveSS(self.driver, 'test_loginWithInvalidUsernameAndPassword')
                            pytest.screenshot_name = ssName
                            logout(self.wait)
                            pytest.fail("login success")
                    try:
                        assert warningMsg==warningText_incorrectPassword
                        ssName = saveSS(self.driver, 'test_loginWithInvalidUsernameAndPassword')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_loginWithInvalidUsernameAndPassword')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_loginWithInvalidUsernameAndPassword')
                    pytest.screenshot_name = ssName
                    pytest.fail("loginBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_loginWithInvalidUsernameAndPassword')
                pytest.screenshot_name = ssName
                pytest.fail("pWordField not found")
        else:
            ssName = saveSS(self.driver, 'test_loginWithInvalidUsernameAndPassword')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
    def test_loginWithValidCredentials(self):
        title='verify that the user is able to login with a valid credentials'
        #pytest.title = title
        self.driver.refresh()
        uNameField = self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys(uName_std_user)
            pWordField = self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys(pWord)
                loginBtn = self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    try:
                        pageTitle=self.visibilityOfEltByXpath(xpath_title)
                        if pageTitle is not None:
                            try:
                                assert pageTitle.text=='Products'
                                ssName = saveSS(self.driver, 'test_loginWithValidCredentials')
                                pytest.screenshot_name = ssName
                                logout(self.wait)
                            except AssertionError as e:
                                ssName = saveSS(self.driver, 'test_loginWithValidCredentials')
                                pytest.screenshot_name = ssName
                                raise
                    except TimeoutException:
                        ssName = saveSS(self.driver, 'test_loginWithValidCredentials')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_loginWithValidCredentials')
                    pytest.screenshot_name = ssName
                    pytest.fail("loginBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_loginWithValidCredentials')
                pytest.screenshot_name = ssName
                pytest.fail("pWordField not found")
        else:
            ssName = saveSS(self.driver, 'test_loginWithValidCredentials')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
            
    def test_blockedUserUnableToLogin(self):
        title='verify that the blocked user is unable to login'
        #pytest.title = title
        self.driver.refresh()
        uNameField = self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys(uName_locked_out_user)
            pWordField = self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys(pWord)
                loginBtn = self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    warningMsg=""
                    try:
                        warningMsg = self.presOfEltByTagName(tag_warningLabel).text
                    except TimeoutException:
                        pageTitle = self.presOfEltByXpath(xpath_title)
                        if pageTitle.is_displayed():
                            ssName = saveSS(self.driver, 'test_blockedUserUnableToLogin')
                            pytest.screenshot_name = ssName
                            logout(self.wait)
                            raise
                    try:
                        assert warningMsg==warningText_lockedOutUser
                        ssName = saveSS(self.driver, 'test_blockedUserUnableToLogin')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_blockedUserUnableToLogin')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_blockedUserUnableToLogin')
                    pytest.screenshot_name = ssName
                    pytest.fail("loginBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_blockedUserUnableToLogin')
                pytest.screenshot_name = ssName
                pytest.fail("pWordField not found")
        else:
            ssName = saveSS(self.driver, 'test_blockedUserUnableToLogin')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
    def test_uNameFieldCaseSensitive(self):
        title='verify that the username field is case sensitive'
        #pytest.title = title
        self.driver.refresh()
        uNameField = self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys(uName_std_user.upper())
            pWordField = self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys(pWord)
                loginBtn = self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    warningMsg=""
                    try:
                        warningMsg = self.presOfEltByTagName(tag_warningLabel).text
                    except TimeoutException:
                        pageTitle = self.presOfEltByXpath(xpath_title)
                        if pageTitle.is_displayed():
                            ssName = saveSS(self.driver, 'test_uNameFieldCaseSensitive')
                            pytest.screenshot_name = ssName
                            logout(self.wait)
                            pytest.fail("login success")
                    try:
                        assert warningMsg==warningText_incorrectUsername
                        ssName = saveSS(self.driver, 'test_uNameFieldCaseSensitive')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_uNameFieldCaseSensitive')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_uNameFieldCaseSensitive')
                    pytest.screenshot_name = ssName
                    pytest.fail("loginBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_uNameFieldCaseSensitive')
                pytest.screenshot_name = ssName
                pytest.fail("pWordField not found")
        else:
            ssName = saveSS(self.driver, 'test_uNameFieldCaseSensitive')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
    def test_pWordFieldCaseSensitive(self):
        title='verify that the password field is case sensitive'
        #pytest.title = title
        self.driver.refresh()
        uNameField = self.presOfEltById(id_uNameField)
        if uNameField is not None:
            uNameField.send_keys(uName_std_user)
            pWordField = self.presOfEltById(id_pWordField)
            if pWordField is not None:
                pWordField.send_keys(pWord.upper())
                loginBtn = self.clickabilityOfEltById(id_loginBtn)
                if loginBtn is not None:
                    loginBtn.click()
                    warningMsg = ""
                    try:
                        warningMsg = self.presOfEltByTagName(tag_warningLabel).text
                    except TimeoutException:
                        pageTitle = self.presOfEltByXpath(xpath_title)
                        if pageTitle.is_displayed():
                            ssName = saveSS(self.driver, 'test_pWordFieldCaseSensitive')
                            pytest.screenshot_name = ssName
                            logout(self.wait)
                            pytest.fail("login success")
                    try:
                        assert warningMsg == warningText_incorrectPassword
                        ssName = saveSS(self.driver, 'test_pWordFieldCaseSensitive')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_pWordFieldCaseSensitive')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_pWordFieldCaseSensitive')
                    pytest.screenshot_name = ssName
                    pytest.fail("loginBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_pWordFieldCaseSensitive')
                pytest.screenshot_name = ssName
                pytest.fail("pWordField not found")
        else:
            ssName = saveSS(self.driver, 'test_pWordFieldCaseSensitive')
            pytest.screenshot_name = ssName
            pytest.fail("uNameField not found")
        
        
    
                              

        
        
        