from time import sleep
import pytest
from data.locators import dashboard
from base import saveScreenShots
from testcases import getElts

eltLocator=getElts.Get_Elts
saveSS=saveScreenShots.saveScreenshot

elts=dashboard.elements
pageTitle=elts['pageTitle']
sectionHeading=elts['sectionHeading']

sortOrders=dashboard.sortOrders
className=dashboard.className
productNameClass=className['productNameClass']
productPriceClass=className['productPriceClass']
yourCartItemNamesClass=className['yourCartItemNamesClass']
yourCartItemPricesClass=className['yourCartItemPricesClass']

xpaths=dashboard.xpaths
xpath_pageLogo=xpaths['pageLogo']
xpath_sectionHeading=xpaths['sectionHeading']
xpath_sortContainer=xpaths['sortContainer']
xpath_s0=xpaths['s0']
xpath_s1=xpaths['s1']
xpath_s2=xpaths['s2']
xpath_s3=xpaths['s3']
xpath_backpackImg=xpaths['backpackImg']
xpath_backpackProdName=xpaths['backpackProdName']
xpath_backpackProdPrice=xpaths['backpackProdPrice']
xpath_backpackAddToCartBtn=xpaths['backpackAddToCartBtn']
xpath_backpackRemoveBtn=xpaths['backpackRemoveBtn']
xpath_cartBadge=xpaths['cartBadge']
xpath_bikeLightImg=xpaths['bikeLightImg']
xpath_bikeLightName=xpaths['bikeLightName']
xpath_bikeLightPrice=xpaths['bikeLightPrice']
xpath_bikeLightAddToCart=xpaths['bikeLightAddToCart']
xpath_shoppingCartLink=xpaths['shoppingCartLink']
xpath_bikeLightAddToCartBtn=xpaths['bikeLightAddToCartBtn']
xpath_bikeLightRemoveBtn=xpaths['bikeLightRemoveBtn']
xpath_tShirtImg=xpaths['tShirtImg']
xpath_tShirtName=xpaths['tShirtName']
xpath_tShirtPrice=xpaths['tShirtPrice']
xpath_tShirtAddToCart=xpaths['tShirtAddToCart']
xpath_tShirtRemoveBtn=xpaths['tShirtRemoveBtn']
xpath_onesieImg=xpaths['onesieImg']
xpath_onesieName=xpaths['onesieName']
xpath_onesiePrice=xpaths['onesiePrice']
xpath_onesieAddToCart=xpaths['onesieAddToCart']
xpath_onesieRemoveBtn=xpaths['onesieRemoveBtn']
xpath_cartIcon=xpaths['cartIcon']
xpath_yourCartPageTitle=xpaths['yourCartPageTitle']
xpath_priceOfBackPackInCart=xpaths['priceOfBackPackInCart']
xpath_priceOfBikeLightInCart=xpaths['priceOfBikeLightInCart']
xpath_priceOfTshirtInCart=xpaths['priceOfTshirtInCart']
xpath_priceOfOnesieInCart=xpaths['priceOfOnesieInCart']
xpath_continueShoppingBtn=xpaths['continueShoppingBtn']
xpath_checkoutBtn=xpaths['checkoutBtn']
xpath_firstNameField=xpaths['firstNameField']
xpath_lastNameField=xpaths['lastNameField']
xpath_zipCodeField=xpaths['zipCodeField']
xpath_cancelBtn=xpaths['cancelBtn']
xpath_continueBtn=xpaths['continueBtn']
xpath_errorMsgFirstName=xpaths['errorMsgFirstName']
xpath_errorMsgLastName=xpaths['errorMsgLastName']
xpath_errorMsgZipCodeField=xpaths['errorMsgZipCodeField']

backpackProdName=''
backpackProdPrice=''
bikeLightName=''
bikeLightPrice=''
tShirtName=''
tShirtPrice=''
onesieName=''
onesiePrice=''

addedItems=[]

n=0


def is_alphabetically_ascending(string_list):

    if not string_list or len(string_list) <= 1:
        return True

    for i in range(len(string_list) - 1):
        if string_list[i] > string_list[i+1]:
            return False
    return True

def is_numerically_ascending(float_list):
    if not float_list or len(float_list) <= 1:
        return True
    for i in range(len(float_list) - 1):
        if float_list[i]>float_list[i+1]:
            return False
    return True

def is_numerically_descending(float_list):
    if not float_list or len(float_list) <= 1:
        return True
    for i in range(len(float_list) - 1):
        if float_list[i]<float_list[i+1]:
            return False
    return True


def is_alphabetically_descending(string_list):

    if not string_list or len(string_list) <= 1:
        return True

    for i in range(len(string_list) - 1):
        if string_list[i] < string_list[i+1]:
            return False
    return True

#@pytest.mark.skip
class Test_dashboardPage:
    driver=None
    wait=None
    presOfEltByXpath=None
    presOfAllEltsByClass=None
    visibilityOfEltByXpath=None
    clickabilityOfEltByXpath=None
    presOfEltById=None
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self,request, setup_driver):
        request.cls.driver, request.cls.wait = setup_driver
        request.cls.locator=eltLocator(request.cls.wait)
        locatorClass=request.cls.locator
        request.cls.presOfEltByXpath = locatorClass.presOfEltByXpath
        request.cls.presOfAllEltsByClass= locatorClass.presOfAllEltsByClass
        request.cls.visibilityOfEltByXpath = locatorClass.visibilityOfEltByXpath
        request.cls.clickabilityOfEltByXpath=locatorClass.clickabilityOfEltByXpath
        request.cls.presOfEltById=locatorClass.presOfEltById

    def test_dashboardPageTitle(self):
        title='Verify that the page header displays "Swag Labs".'
        #pytest.title = title
        pageLogoTitle=self.visibilityOfEltByXpath(xpath_pageLogo)
        if pageLogoTitle is not None:
            try:
                assert pageLogoTitle.text==pageTitle
                ssName = saveSS(self.driver, 'test_dashboardPageTitle')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName=saveSS(self.driver,'test_dashboardPageTitle')
                pytest.screenshot_name=ssName
                raise
        else:
            saveSS(self.driver, 'test_dashboardPageTitle')
            ssName = saveSS(self.driver, 'test_dashboardPageTitle')
            pytest.screenshot_name = ssName
            pytest.fail("The element pageLogoTitle not found")
    def test_dashboardPageTitleBrowserTab(self):
        title ='Verify that the page title in the browser tab is "Swag Labs".'
        #pytest.title = title
        try:
            assert self.driver.title==pageTitle
            ssName = saveSS(self.driver, 'test_dashboardPageTitleBrowserTab')
            pytest.screenshot_name = ssName
        except AssertionError as e:
            ssName = saveSS(self.driver, 'test_dashboardPageTitleBrowserTab')
            pytest.screenshot_name = ssName
            raise

    def test_sectionHeading(self):
        title='Verify that the section heading displays "Products".'
        #pytest.title = title
        sectionHeading1=self.visibilityOfEltByXpath(xpath_sectionHeading)
        if sectionHeading1 is not None:
            try:
                assert sectionHeading1.text==sectionHeading
                ssName = saveSS(self.driver, 'test_sectionHeading')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_sectionHeading')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_sectionHeading')
            pytest.screenshot_name = ssName
            pytest.fail("sectionHeading1 not found")
    
    def test_sortOrders(self):
        title='Verify that the  sort orders in the dropdown are "Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)".'
        #pytest.title = title
        sortDropdownString=self.visibilityOfEltByXpath(xpath_sortContainer)
        if sortDropdownString is not None:
            sortDropdownString=sortDropdownString.text
            sortDropdownList = sortDropdownString.split("\n")
            #print(sortDropdownList)
            try:
                assert len(sortDropdownList)==4 and sortOrders['s0'] in sortDropdownList and sortOrders['s1'] in sortDropdownList and sortOrders['s2'] in sortDropdownList and sortOrders['s3'] in sortDropdownList
                ssName = saveSS(self.driver, 'test_sortOrders')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_sortOrders')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_sortOrders')
            pytest.screenshot_name = ssName
            pytest.fail("sortDropdownString not found")
    def test_defaultSortOrder(self):
        title='Verify that the default sort order in the dropdown is "Name (A to Z)".'
        #pytest.title = title
        sortDropdownString=self.visibilityOfEltByXpath(xpath_sortContainer)
        if sortDropdownString is not None:
            sortDropdownString=sortDropdownString.text
            sortDropdownList = sortDropdownString.split("\n")
            defaultSortOrder=sortDropdownList[0]
            eltsInClass=self.presOfAllEltsByClass(productNameClass)
            names = []
            for itm in eltsInClass:
                name = itm.text
                names.append(name)
            try:
                assert defaultSortOrder==sortOrders['s0'] and is_alphabetically_ascending(names)
                ssName = saveSS(self.driver, 'test_defaultSortOrder')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_defaultSortOrder')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_defaultSortOrder')
            pytest.screenshot_name = ssName
            pytest.fail("sortDropdownString is not found")

    def test_nameDescOrderSort(self):
        title='Verify that selecting "Name (Z to A)" reorders the products alphabetically in descending order.'
        #pytest.title = title
        sortDropdown=self.visibilityOfEltByXpath(xpath_sortContainer)
        if sortDropdown is not None:
            sortDropdown.click()
            sleep(1)
            option1=self.visibilityOfEltByXpath(xpath_s1)
            if option1 is not None:
                option1.click()
                sleep(1)
                eltsInClass=self.presOfAllEltsByClass(productNameClass)
                if eltsInClass is not None:
                    names = []
                    for itm in eltsInClass:
                        name = itm.text
                        names.append(name)
                    try:
                        assert is_alphabetically_descending(names)
                        ssName = saveSS(self.driver, 'test_nameDescOrderSort')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_nameDescOrderSort')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_nameDescOrderSort')
                    pytest.screenshot_name = ssName
                    pytest.fail("eltsInClass not found")
            else:
                ssName = saveSS(self.driver, 'test_nameDescOrderSort')
                pytest.screenshot_name = ssName
                pytest.fail("option1 not found")
        else:
            ssName = saveSS(self.driver, 'test_nameDescOrderSort')
            pytest.screenshot_name = ssName
            pytest.fail("sortDropdown not found")

    def test_priceDescOrder(self):
        title='Verify that selecting "Price (low to high)" reorders the products by price from lowest to highest.'
        #pytest.title = title
        sortDropdown=self.visibilityOfEltByXpath(xpath_sortContainer)
        if sortDropdown is not None:
            sortDropdown.click()
            sleep(1)
            option2=self.visibilityOfEltByXpath(xpath_s2)
            if option2 is not None:
                option2.click()
                sleep(1)
                eltsInClass=self.presOfAllEltsByClass(productPriceClass)
                if eltsInClass is not None:
                    pricesWithSymbol = []
                    for itm in eltsInClass:
                        name = itm.text
                        pricesWithSymbol.append(name)
                    prices = []
                    for elt in pricesWithSymbol:
                        price = elt[1:]
                        price = float(price)
                        prices.append(price)
                    #print(prices)
                    try:
                        assert is_numerically_ascending(prices)
                        ssName = saveSS(self.driver, 'test_priceDescOrder')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_priceDescOrder')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_priceDescOrder')
                    pytest.screenshot_name = ssName
                    pytest.fail("eltsInClass is not found")
            else:
                ssName = saveSS(self.driver, 'test_priceDescOrder')
                pytest.screenshot_name = ssName
                pytest.fail("option2 is not found")
        else:
            ssName = saveSS(self.driver, 'test_priceDescOrder')
            pytest.screenshot_name = ssName
            pytest.fail("sortDropdown is not found")

    def test_priceAsceOrder(self):
        title='Verify that selecting "Price (high to low)" reorders the products by price from highest to lowest.'
        #pytest.title = title
        sortDropdown=self.visibilityOfEltByXpath(xpath_sortContainer)
        if sortDropdown is not None:
            sortDropdown.click()
            sleep(1)
            option3=self.visibilityOfEltByXpath(xpath_s3)
            if option3 is not None:
                option3.click()
                sleep(1)
                eltsInClass=self.presOfAllEltsByClass(productPriceClass)
                if eltsInClass is not None:
                    pricesWithSymbol = []
                    for itm in eltsInClass:
                        name = itm.text
                        pricesWithSymbol.append(name)
                    prices = []
                    for elt in pricesWithSymbol:
                        price = elt[1:]
                        price = float(price)
                        prices.append(price)
                    #print(prices)
                    try:
                        assert is_numerically_descending(prices)
                        ssName = saveSS(self.driver, 'test_priceAsceOrder')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_priceAsceOrder')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_priceAsceOrder')
                    pytest.screenshot_name = ssName
                    pytest.fail("eltsInClass is not found")
            else:
                ssName = saveSS(self.driver, 'test_priceAsceOrder')
                pytest.screenshot_name = ssName
                pytest.fail("option3 is not found")
        else:
            ssName = saveSS(self.driver, 'test_priceAsceOrder')
            pytest.screenshot_name = ssName
            pytest.fail("sortDropdown is not found")

    def test_backpackImg(self):
        title='Verify that the backpack image is displayed.'
        #pytest.title = title
        self.driver.refresh()
        sleep(1)
        backpackImg=self.presOfEltByXpath(xpath_backpackImg)
        if backpackImg is not None:
            try:
                assert backpackImg and backpackImg.get_attribute("alt")=="Sauce Labs Backpack"
                ssName = saveSS(self.driver, 'test_backpackImg')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_backpackImg')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_backpackImg')
            pytest.screenshot_name = ssName
            pytest.fail("backpackImg is not found")

    def test_backpackProdName(self):
        global backpackProdName
        title='Verify that the backpack name is "Sauce Labs Backpack".'
        #pytest.title = title
        backpackProdName=self.presOfEltByXpath(xpath_backpackProdName)
        if backpackProdName is not None:
            backpackProdName=backpackProdName.text
            try:
                assert backpackProdName=='Sauce Labs Backpack'
                ssName = saveSS(self.driver, 'test_backpackProdName')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_backpackProdName')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_backpackProdName')
            pytest.screenshot_name = ssName
            pytest.fail("backpackProdName is not found")

    def test_backpackProdPrice(self):
        global backpackProdPrice
        title='Verify that the backpack price is "$29.99".'
        #pytest.title = title
        backpackProdPrice=self.presOfEltByXpath(xpath_backpackProdPrice)
        if backpackProdPrice is not None:
            backpackProdPrice=backpackProdPrice.text
            try:
                assert backpackProdPrice=='$29.99'
                ssName = saveSS(self.driver, 'test_backpackProdPrice')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_backpackProdPrice')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_backpackProdPrice')
            pytest.screenshot_name = ssName
            pytest.fail("backpackProdPrice is not found")
    def test_backpackAddToCartBtn(self):
        title='Verify that the "Add to cart" button for the backpack is present and clickable.'
        #pytest.title = title
        backpackAddToCartBtn=self.clickabilityOfEltByXpath(xpath_backpackAddToCartBtn)
        if backpackAddToCartBtn is not None:
            try:
                assert backpackAddToCartBtn.is_displayed() and backpackAddToCartBtn.is_enabled()
                ssName = saveSS(self.driver, 'test_backpackAddToCartBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_backpackAddToCartBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_backpackAddToCartBtn')
            pytest.screenshot_name = ssName
            pytest.fail("backpackAddToCartBtn is not found")

    def test_backpackAddToCartFunc(self):
        global n
        title = 'Verify that clicking "Add to cart" adds the backpack to the shopping cart.'
        #pytest.title = title
        backpackAddToCartBtn=self.clickabilityOfEltByXpath(xpath_backpackAddToCartBtn)
        if backpackAddToCartBtn is not None:
            backpackAddToCartBtn.click()
            n+=1
            sleep(1)
            removeBtn=self.clickabilityOfEltByXpath(xpath_backpackRemoveBtn)
            if removeBtn is not None:
                removeBtnLabel=removeBtn.text
                cartItemsCount=self.visibilityOfEltByXpath(xpath_cartBadge)
                if cartItemsCount is not None:
                    try:
                        assert removeBtnLabel=='Remove' and cartItemsCount.text==str(n)
                        ssName = saveSS(self.driver, 'test_backpackAddToCartFunc')
                        pytest.screenshot_name = ssName
                        newItem=dict(
                            name=backpackProdName,
                            price=backpackProdPrice
                        )
                        addedItems.append(newItem)
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_backpackAddToCartFunc')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_backpackAddToCartFunc')
                    pytest.screenshot_name = ssName
                    pytest.fail("cartItemsCount is not found")
            else:
                ssName = saveSS(self.driver, 'test_backpackAddToCartFunc')
                pytest.screenshot_name = ssName
                pytest.fail("removeBtn is not found")
        else:
            ssName = saveSS(self.driver, 'test_backpackAddToCartFunc')
            pytest.screenshot_name = ssName
            pytest.fail("backpackAddToCartBtn is not found")

    def test_bikeLightImg(self):
        title='Verify that bike light is available in the cart.'
        #pytest.title = title
        bikeLightImg=self.presOfEltByXpath(xpath_bikeLightImg)
        if bikeLightImg is not None:
            try:
                assert bikeLightImg and bikeLightImg.get_attribute("alt")=="Sauce Labs Bike Light"
                ssName = saveSS(self.driver, 'test_bikeLightImg')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_bikeLightImg')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_bikeLightImg')
            pytest.screenshot_name = ssName
            pytest.fail("bikeLightImg is not found")

    def test_bikeLightName(self):
        global bikeLightName
        title='Verify that the bike light name is "Sauce Labs Bike Light".'
        #pytest.title = title
        bikeLightName=self.presOfEltByXpath(xpath_bikeLightName)
        if bikeLightName is not None:
            bikeLightName=bikeLightName.text
            try:
                assert bikeLightName=="Sauce Labs Bike Light"
                ssName = saveSS(self.driver, 'test_bikeLightName')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_bikeLightName')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_bikeLightName')
            pytest.screenshot_name = ssName
            pytest.fail("bikeLightName is not found")
    def test_bikeLightPrice(self):
        global bikeLightPrice
        title='Verify that the bike light price is "$9.99".'
        #pytest.title = title
        bikeLightPrice=self.presOfEltByXpath(xpath_bikeLightPrice)
        if bikeLightPrice is not None:
            bikeLightPrice=bikeLightPrice.text
            try:
                assert bikeLightPrice=="$9.99"
                ssName = saveSS(self.driver, 'test_bikeLightPrice')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_bikeLightPrice')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_bikeLightPrice')
            pytest.screenshot_name = ssName
            pytest.fail("bikeLightPrice is not found")

    def test_bikeLightAddToCartBtn(self):
        title='Verify that the "Add to cart" button for the bike light is present and clickable.'
        #pytest.title = title
        bikeLightAddToCartBtn=self.clickabilityOfEltByXpath(xpath_bikeLightAddToCart)
        if bikeLightAddToCartBtn is not None:
            try:
                assert bikeLightAddToCartBtn.is_displayed() and bikeLightAddToCartBtn.is_enabled()
                ssName = saveSS(self.driver, 'test_bikeLightAddToCartBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_bikeLightAddToCartBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_bikeLightAddToCartBtn')
            pytest.screenshot_name = ssName
            pytest.fail("bikeLightAddToCartBtn is not found")

    def test_bikeLightAddToCartFunc(self):
        global n
        title = 'Verify that clicking "Add to cart" adds the bike light to the shopping cart.'
        #pytest.title = title
        bikeLightAddToCartBtn=self.clickabilityOfEltByXpath(xpath_bikeLightAddToCartBtn)
        if bikeLightAddToCartBtn is not None:
            bikeLightAddToCartBtn.click()
            n+=1
            sleep(1)
            removeBtn=self.clickabilityOfEltByXpath(xpath_bikeLightRemoveBtn)
            if removeBtn is not None:
                removeBtnLabel=removeBtn.text
                cartItemsCount=self.visibilityOfEltByXpath(xpath_cartBadge)
                if cartItemsCount is not None:
                    try:
                        assert removeBtnLabel=='Remove' and cartItemsCount.text==str(n)
                        ssName = saveSS(self.driver, 'test_bikeLightAddToCartFunc')
                        pytest.screenshot_name = ssName
                        newItem=dict(
                            name=bikeLightName,
                            price=bikeLightPrice
                        )
                        addedItems.append(newItem)
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_bikeLightAddToCartFunc')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_bikeLightAddToCartFunc')
                    pytest.screenshot_name = ssName
                    pytest.fail("cartItemsCount is not found")
            else:
                ssName = saveSS(self.driver, 'test_bikeLightAddToCartFunc')
                pytest.screenshot_name = ssName
                pytest.fail("removeBtn is not found")
        else:
            ssName = saveSS(self.driver, 'test_bikeLightAddToCartFunc')
            pytest.screenshot_name = ssName
            pytest.fail("bikeLightAddToCartBtn is not found")

    def test_tShirtImg(self):
        title='Verify that T-Shirt is available in the cart.'
        #pytest.title = title
        tShirtImg=self.presOfEltByXpath(xpath_tShirtImg)
        if tShirtImg is not None:
            try:
                assert tShirtImg and tShirtImg.get_attribute("alt")=="Sauce Labs Bolt T-Shirt"
                ssName = saveSS(self.driver, 'test_tShirtImg')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_tShirtImg')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_tShirtImg')
            pytest.screenshot_name = ssName
            pytest.fail("tShirtImg is not found")

    def test_tShirtName(self):
        global tShirtName
        title='Verify that the T-Shirt name is "Sauce Labs Bolt T-Shirt".'
        #pytest.title = title
        tShirtName=self.presOfEltByXpath(xpath_tShirtName)
        if tShirtName is not None:
            tShirtName=tShirtName.text
            try:
                assert tShirtName=="Sauce Labs Bolt T-Shirt"
                ssName = saveSS(self.driver, 'test_tShirtName')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_tShirtName')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_tShirtName')
            pytest.screenshot_name = ssName
            pytest.fail("bikeLightName is not found")
    def test_tShirtPrice(self):
        global tShirtPrice
        title='Verify that the T-Shirt price is "$15.99".'
        #pytest.title = title
        tShirtPrice=self.presOfEltByXpath(xpath_tShirtPrice)
        if tShirtPrice is not None:
            tShirtPrice=tShirtPrice.text
            try:
                assert tShirtPrice=="$15.99"
                ssName = saveSS(self.driver, 'test_tShirtPrice')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_tShirtPrice')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_tShirtPrice')
            pytest.screenshot_name = ssName
            pytest.fail("tShirtPrice is not found")

    def test_tShirtAddToCartBtn(self):
        title='Verify that the "Add to cart" button for the T-Shirt is present and clickable.'
        #pytest.title = title
        tShirtAddToCartBtn=self.clickabilityOfEltByXpath(xpath_tShirtAddToCart)
        if tShirtAddToCartBtn is not None:
            try:
                assert tShirtAddToCartBtn.is_displayed() and tShirtAddToCartBtn.is_enabled()
                ssName = saveSS(self.driver, 'test_tShirtAddToCartBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_tShirtAddToCartBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_tShirtAddToCartBtn')
            pytest.screenshot_name = ssName
            pytest.fail("tShirtAddToCartBtn is not found")

    def test_tShirtAddToCartFunc(self):
        global n
        title = 'Verify that clicking "Add to cart" adds the T-Shirt to the shopping cart.'
        #pytest.title = title
        tShirtAddToCartBtn=self.clickabilityOfEltByXpath(xpath_tShirtAddToCart)
        if tShirtAddToCartBtn is not None:
            tShirtAddToCartBtn.click()
            n+=1
            sleep(1)
            removeBtn=self.clickabilityOfEltByXpath(xpath_tShirtRemoveBtn)
            if removeBtn is not None:
                removeBtnLabel=removeBtn.text
                cartItemsCount=self.visibilityOfEltByXpath(xpath_cartBadge)
                if cartItemsCount is not None:
                    try:
                        assert removeBtnLabel=='Remove' and cartItemsCount.text==str(n)
                        ssName = saveSS(self.driver, 'test_tShirtAddToCartFunc')
                        pytest.screenshot_name = ssName
                        newItem=dict(
                            name=tShirtName,
                            price=tShirtPrice
                        )
                        addedItems.append(newItem)
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_tShirtAddToCartFunc')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_tShirtAddToCartFunc')
                    pytest.screenshot_name = ssName
                    pytest.fail("cartItemsCount is not found")
            else:
                ssName = saveSS(self.driver, 'test_tShirtAddToCartFunc')
                pytest.screenshot_name = ssName
                pytest.fail("removeBtn is not found")
        else:
            ssName = saveSS(self.driver, 'test_tShirtAddToCartFunc')
            pytest.screenshot_name = ssName
            pytest.fail("tShirtAddToCartBtn is not found")

    def test_onesieImg(self):
        title='Verify that Onesie is available in the cart.'
        #pytest.title = title
        onesieImg=self.presOfEltByXpath(xpath_onesieImg)
        if onesieImg is not None:
            try:
                assert onesieImg and onesieImg.get_attribute("alt")=="Sauce Labs Onesie"
                ssName = saveSS(self.driver, 'test_onesieImg')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_onesieImg')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_onesieImg')
            pytest.screenshot_name = ssName
            pytest.fail("onesieImg is not found")

    def test_onesieName(self):
        global onesieName
        title='Verify that the Onesie name is "Sauce Labs Bolt T-Shirt".'
        #pytest.title = title
        onesieName=self.presOfEltByXpath(xpath_onesieName)
        if onesieName is not None:
            onesieName=onesieName.text
            try:
                assert onesieName=="Sauce Labs Onesie"
                ssName = saveSS(self.driver, 'test_onesieName')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_onesieName')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_onesieName')
            pytest.screenshot_name = ssName
            pytest.fail("onesieName is not found")
    def test_onesiePrice(self):
        global onesiePrice
        title='Verify that the Onesie price is "$7.99".'
        #pytest.title = title
        onesiePrice=self.presOfEltByXpath(xpath_onesiePrice)
        if onesiePrice is not None:
            onesiePrice=onesiePrice.text
            try:
                assert onesiePrice=="$7.99"
                ssName = saveSS(self.driver, 'test_onesiePrice')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_onesiePrice')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_onesiePrice')
            pytest.screenshot_name = ssName
            pytest.fail("onesiePrice is not found")

    def test_onesieAddToCartBtn(self):
        title='Verify that the "Add to cart" button for the Onesie is present and clickable.'
        #pytest.title = title
        onesieAddToCartBtn=self.clickabilityOfEltByXpath(xpath_onesieAddToCart)
        if onesieAddToCartBtn is not None:
            try:
                assert onesieAddToCartBtn.is_displayed() and onesieAddToCartBtn.is_enabled()
                ssName = saveSS(self.driver, 'test_onesieAddToCartBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_onesieAddToCartBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_onesieAddToCartBtn')
            pytest.screenshot_name = ssName
            pytest.fail("onesieAddToCartBtn is not found")

    def test_onesieAddToCartFunc(self):
        global n
        title = 'Verify that clicking "Add to cart" adds the Onesie to the shopping cart.'
        #pytest.title = title
        onesieAddToCartBtn=self.clickabilityOfEltByXpath(xpath_onesieAddToCart)
        if onesieAddToCartBtn is not None:
            onesieAddToCartBtn.click()
            n+=1
            sleep(1)
            removeBtn=self.clickabilityOfEltByXpath(xpath_onesieRemoveBtn)
            if removeBtn is not None:
                removeBtnLabel=removeBtn.text
                cartItemsCount=self.visibilityOfEltByXpath(xpath_cartBadge)
                if cartItemsCount is not None:
                    try:
                        assert removeBtnLabel=='Remove' and cartItemsCount.text==str(n)
                        ssName = saveSS(self.driver, 'test_onesieAddToCartFunc')
                        pytest.screenshot_name = ssName
                        newItem=dict(
                            name=onesieName,
                            price=onesiePrice
                        )
                        addedItems.append(newItem)
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_onesieAddToCartFunc')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_onesieAddToCartFunc')
                    pytest.screenshot_name = ssName
                    pytest.fail("cartItemsCount is not found")
            else:
                ssName = saveSS(self.driver, 'test_onesieAddToCartFunc')
                pytest.screenshot_name = ssName
                pytest.fail("removeBtn is not found")
        else:
            ssName = saveSS(self.driver, 'test_onesieAddToCartFunc')
            pytest.screenshot_name = ssName
            pytest.fail("onesieAddToCartBtn is not found")

    def test_cartIconEnabled(self):
        title="Verify that cart icon is enabled."
        #pytest.title = title
        cartIcon = self.presOfEltByXpath(xpath_cartIcon)
        if cartIcon is not None:
            try:
                assert cartIcon.is_displayed() and cartIcon.is_enabled()
                ssName = saveSS(self.driver, 'test_cartIconEnabled')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_cartIconEnabled')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_cartIconEnabled')
            pytest.screenshot_name = ssName
            pytest.fail("cartIcon not found")

    def test_clickOnCartIconOpensYourCartPage(self):
        title="Verify that clicking on the cart icon opens the your cart page."
        #pytest.title = title
        cartIcon=self.presOfEltByXpath(xpath_cartIcon)
        if cartIcon is not None:
            cartIcon.click()
            pageTitle1=self.presOfEltByXpath(xpath_yourCartPageTitle)
            if pageTitle1 is not None:
                try:
                    assert pageTitle1.text=="Your Cart"
                    ssName = saveSS(self.driver, 'test_clickOnCartIconOpensYourCartPage')
                    pytest.screenshot_name = ssName
                except AssertionError as e:
                    ssName = saveSS(self.driver, 'test_clickOnCartIconOpensYourCartPage')
                    pytest.screenshot_name = ssName
                    raise
            else:
                ssName = saveSS(self.driver, 'test_clickOnCartIconOpensYourCartPage')
                pytest.screenshot_name = ssName
                pytest.fail("pageTitle1 not found")
        else:
            ssName = saveSS(self.driver, 'test_clickOnCartIconOpensYourCartPage')
            pytest.screenshot_name = ssName
            pytest.fail("cartIcon not found")

    def test_yourCartPageContainsAllAddedItems(self):
        title="Verify that the your cart page contains all added items"
        #pytest.title = title
        classItems=self.presOfAllEltsByClass(yourCartItemNamesClass)
        if classItems is not None:
            nameOfItems=[]
            for itm in classItems:
                name=itm.text
                nameOfItems.append(name)
            if len(nameOfItems)==len(addedItems):
                for elt in addedItems:
                    assert elt['name'] in nameOfItems
                ssName = saveSS(self.driver, 'test_yourCartPageContainsAllAddedItems')
                pytest.screenshot_name = ssName
                #print(nameOfItems)
            else:
                ssName = saveSS(self.driver, 'test_yourCartPageContainsAllAddedItems')
                pytest.screenshot_name = ssName
                pytest.fail("number of added items and items in your cart page is not equal")
        else:
            ssName = saveSS(self.driver, 'test_yourCartPageContainsAllAddedItems')
            pytest.screenshot_name = ssName
            pytest.fail("classItems not found")

    def test_priceOfBackPackInCart(self):
        title='Verify that the price of back pack in your cart page is "$29.99"'
        #pytest.title = title
        priceOfBackPackInCart=self.presOfEltByXpath(xpath_priceOfBackPackInCart)
        if priceOfBackPackInCart is not None:
            try:
                assert priceOfBackPackInCart.text==backpackProdPrice
                ssName = saveSS(self.driver, 'test_priceOfBackPackInCart')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_priceOfBackPackInCart')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_priceOfBackPackInCart')
            pytest.screenshot_name = ssName
            pytest.fail("priceOfBackPackInCart not found")

    def test_priceOfBikeLightInCart(self):
        title='Verify that the price of bike light in your cart page is "$9.99"'
        #pytest.title = title
        priceOfBikeLightInCart=self.presOfEltByXpath(xpath_priceOfBikeLightInCart)
        if priceOfBikeLightInCart is not None:
            try:
                assert priceOfBikeLightInCart.text==bikeLightPrice
                ssName = saveSS(self.driver, 'test_priceOfBikeLightInCart')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_priceOfBikeLightInCart')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_priceOfBikeLightInCart')
            pytest.screenshot_name = ssName
            pytest.fail("priceOfBikeLightInCart not found")

    def test_priceOfTshirtInCart(self):
        title='Verify that the price of T-Shirt in your cart page is "$15.99"'
        #pytest.title = title
        priceOfTshirtInCart=self.presOfEltByXpath(xpath_priceOfTshirtInCart)
        if priceOfTshirtInCart is not None:
            try:
                assert priceOfTshirtInCart.text==tShirtPrice
                ssName = saveSS(self.driver, 'test_priceOfTshirtInCart')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_priceOfTshirtInCart')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_priceOfTshirtInCart')
            pytest.screenshot_name = ssName
            pytest.fail("priceOfTshirtInCart not found")

    def test_priceOfOnesieInCart(self):
        title='Verify that the price of Onesie in your cart page is "$7.99"'
        #pytest.title = title
        priceOfOnesieInCart=self.presOfEltByXpath(xpath_priceOfOnesieInCart)
        if priceOfOnesieInCart is not None:
            try:
                assert priceOfOnesieInCart.text==onesiePrice
                ssName = saveSS(self.driver, 'test_priceOfOnesieInCart')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_priceOfOnesieInCart')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_priceOfOnesieInCart')
            pytest.screenshot_name = ssName
            pytest.fail("priceOfOnesieInCart not found")

    def test_clickOnRemoveBtnForTshirtRemovesItFromCart(self):
        global n
        title='Verify that clicking on the remove button for the T-shirt removes it from your cart list.'
        #pytest.title = title
        removeBtn=self.presOfEltByXpath(xpath_tShirtRemoveBtn)
        if removeBtn is not None:
            if removeBtn.is_displayed() and removeBtn.is_enabled():
                removeBtn.click()
                classItems = self.presOfAllEltsByClass(yourCartItemNamesClass)
                if classItems is not None:
                    nameOfItems = []
                    for itm in classItems:
                        name = itm.text
                        nameOfItems.append(name)
                    try:
                        assert tShirtName not in nameOfItems
                        ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForTshirtRemovesItFromCart')
                        pytest.screenshot_name = ssName
                        n=n-1
                        for i in range(len(addedItems)):
                            if addedItems[i]['name']==tShirtName:
                                addedItems.pop(i)
                                break
                            else:
                                pass
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForTshirtRemovesItFromCart')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForTshirtRemovesItFromCart')
                    pytest.screenshot_name = ssName
                    pytest.fail("classItems not found")
            else:
                ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForTshirtRemovesItFromCart')
                pytest.screenshot_name = ssName
                pytest.fail("removeBtn is not displayed or not enabled")
        else:
            ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForTshirtRemovesItFromCart')
            pytest.screenshot_name = ssName
            pytest.fail("removeBtn not found")

    def test_clickOnContinueShoppingNavigatesToShoppingPage(self):
        title='Verify that clicking "Continue Shopping" button on your cart page navigates to shopping page.'
        #pytest.title = title
        continueShoppingBtn=self.presOfEltByXpath(xpath_continueShoppingBtn)
        if continueShoppingBtn is not None:
            if continueShoppingBtn.is_displayed() and continueShoppingBtn.is_enabled():
                continueShoppingBtn.click()
                pageTitle1=self.presOfEltByXpath(xpath_sectionHeading)
                if pageTitle1 is not None:
                    try:
                        assert pageTitle1.text==sectionHeading
                        ssName = saveSS(self.driver, 'test_clickOnContinueShoppingNavigatesToShoppingPage')
                        pytest.screenshot_name = ssName
                    except AssertionError as e:
                        ssName = saveSS(self.driver, 'test_clickOnContinueShoppingNavigatesToShoppingPage')
                        pytest.screenshot_name = ssName
                        raise
                else:
                    ssName = saveSS(self.driver, 'test_clickOnContinueShoppingNavigatesToShoppingPage')
                    pytest.screenshot_name = ssName
                    pytest.fail("pageTitle1 not found")
            else:
                ssName = saveSS(self.driver, 'test_clickOnContinueShoppingNavigatesToShoppingPage')
                pytest.screenshot_name = ssName
                pytest.fail("continueShoppingBtn is not displayed or not enabled")
        else:
            ssName = saveSS(self.driver, 'test_clickOnContinueShoppingNavigatesToShoppingPage')
            pytest.screenshot_name = ssName
            pytest.fail("continueShoppingBtn not found")

    def test_clickOnRemoveBtnForBikeLightRemovesItFromCart(self):
        title='Verify that clicking on the remove button for the Bike Light removes it from your cart list.'
        #pytest.title = title
        global n
        removeBtn = self.presOfEltByXpath(xpath_bikeLightRemoveBtn)
        if removeBtn is not None:
            if removeBtn.is_displayed() and removeBtn.is_enabled():
                removeBtn.click()
                n = n - 1
                addToCartBtn=self.presOfEltByXpath(xpath_bikeLightAddToCartBtn)
                if addToCartBtn is not None:
                    if addToCartBtn.is_displayed() and addToCartBtn.is_enabled():
                        cartItemsCount = self.visibilityOfEltByXpath(xpath_cartBadge)
                        if cartItemsCount is not None:
                            try:
                                assert addToCartBtn.text=="Add to cart" and cartItemsCount.text==str(n)
                                ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
                                pytest.screenshot_name = ssName
                                for i in range(len(addedItems)):
                                    if addedItems[i]['name'] == bikeLightName:
                                        addedItems.pop(i)
                                        break
                                    else:
                                        pass
                            except AssertionError as e:
                                ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
                                pytest.screenshot_name = ssName
                                raise
                        else:
                            ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
                            pytest.screenshot_name = ssName
                            pytest.fail("cartItemsCount not found")
                    else:
                        ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
                        pytest.screenshot_name = ssName
                        pytest.fail("addToCartBtn is not displayed or not enabled")
                else:
                    ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
                    pytest.screenshot_name = ssName
                    pytest.fail("addToCartBtn not found")
            else:
                ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
                pytest.screenshot_name = ssName
                pytest.fail("removeBtn is not displayed or not enabled")
        else:
            ssName = saveSS(self.driver, 'test_clickOnRemoveBtnForBikeLightRemovesItFromCart')
            pytest.screenshot_name = ssName
            pytest.fail("removeBtn not found")

    def test_bikeLightIsNotAvailableInYourCart(self):
        global n
        title='Verify that Bike Light is not available in your cart list'
        #pytest.title = title
        cartIcon = self.presOfEltByXpath(xpath_cartIcon)
        if cartIcon is not None:
            cartIcon.click()
            classItems = self.presOfAllEltsByClass(yourCartItemNamesClass)
            if classItems is not None:
                nameOfItems = []
                for itm in classItems:
                    name = itm.text
                    nameOfItems.append(name)
                try:
                    assert bikeLightName not in nameOfItems and len(nameOfItems)==n
                    ssName = saveSS(self.driver, 'test_bikeLightIsNotAvailableInYourCart')
                    pytest.screenshot_name = ssName
                except AssertionError as e:
                    ssName = saveSS(self.driver, 'test_bikeLightIsNotAvailableInYourCart')
                    pytest.screenshot_name = ssName
                    raise
            else:
                ssName = saveSS(self.driver, 'test_bikeLightIsNotAvailableInYourCart')
                pytest.screenshot_name = ssName
                pytest.fail("classItems not found")
        else:
            ssName = saveSS(self.driver, 'test_bikeLightIsNotAvailableInYourCart')
            pytest.screenshot_name = ssName
            pytest.fail("cartIcon not found")

    def test_checkoutBtnInYourCartPage(self):
        title='Verify that your cart page has "Checkout" button'
        #pytest.title = title
        checkoutBtn=self.presOfEltByXpath(xpath_checkoutBtn)
        if checkoutBtn is not None:
            try:
                assert checkoutBtn.is_displayed() and checkoutBtn.is_enabled() and checkoutBtn.text=="Checkout"
                ssName = saveSS(self.driver, 'test_checkoutBtnInYourCartPage')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_checkoutBtnInYourCartPage')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_checkoutBtnInYourCartPage')
            pytest.screenshot_name = ssName
            pytest.fail("checkoutBtn not found")

    def test_clickOnCheckoutBtnNavigatesToYourInfoPage(self):
        title='Verify that clicking on Checkout button navigates to "Your information" page'
        #pytest.title = title
        checkoutBtn = self.presOfEltByXpath(xpath_checkoutBtn)
        checkoutBtn.click()
        checkoutYourInfoPageTitle=self.presOfEltByXpath(xpath_sectionHeading)
        if checkoutYourInfoPageTitle is not None:
            try:
                assert checkoutYourInfoPageTitle.text=="Checkout: Your Information"
                ssName = saveSS(self.driver, 'test_clickOnCheckoutBtnNavigatesToYourInfoPage')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_clickOnCheckoutBtnNavigatesToYourInfoPage')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_clickOnCheckoutBtnNavigatesToYourInfoPage')
            pytest.screenshot_name = ssName
            pytest.fail("checkoutYourInfoPageTitle not found")

    def test_yourInfoPageHasFirstNameField(self):
        title='Verify that the your information page has first name field with placeholder text "First Name"'
        #pytest.title = title
        firstNameField=self.presOfEltByXpath(xpath_firstNameField)
        if firstNameField is not None:
            try:
                assert firstNameField.is_enabled() and firstNameField.get_attribute("placeholder")=="First Name"
                ssName = saveSS(self.driver, 'test_yourInfoPageHasFirstNameField')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_yourInfoPageHasFirstNameField')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_yourInfoPageHasFirstNameField')
            pytest.screenshot_name = ssName
            pytest.fail("firstNameField not found")

    def test_yourInfoPageHasLastNameField(self):
        title='Verify that the your information page has last name field with placeholder text "Last Name"'
        #pytest.title = title
        lastNameField=self.presOfEltByXpath(xpath_lastNameField)
        if lastNameField is not None:
            try:
                assert lastNameField.is_enabled() and lastNameField.get_attribute("placeholder")=="Last Name"
                ssName = saveSS(self.driver, 'test_yourInfoPageHasLastNameField')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_yourInfoPageHasLastNameField')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_yourInfoPageHasLastNameField')
            pytest.screenshot_name = ssName
            pytest.fail("lastNameField not found")

    def test_yourInfoPageHasZipCodeField(self):
        title='Verify that the your information page has zip code field with placeholder text "Zip/Postal Code"'
        #pytest.title = title
        zipCodeField=self.presOfEltByXpath(xpath_zipCodeField)
        if zipCodeField is not None:
            try:
                assert zipCodeField.is_enabled() and zipCodeField.get_attribute("placeholder")=="Zip/Postal Code"
                ssName = saveSS(self.driver, 'test_yourInfoPageHasZipCodeField')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_yourInfoPageHasZipCodeField')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_yourInfoPageHasZipCodeField')
            pytest.screenshot_name = ssName
            pytest.fail("zipCodeField not found")

    def test_yourInfoPageHasCancelBtn(self):
        title='Verify that the your information page has "Cancel" button'
        #pytest.title = title
        cancelBtn=self.presOfEltByXpath(xpath_cancelBtn)
        if cancelBtn is not None:
            try:
                assert cancelBtn.is_displayed() and cancelBtn.is_enabled() and cancelBtn.text=='Cancel'
                ssName = saveSS(self.driver, 'test_yourInfoPageHasCancelBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_yourInfoPageHasCancelBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_yourInfoPageHasCancelBtn')
            pytest.screenshot_name = ssName
            pytest.fail("cancelBtn not found")
    def test_clickingOnCancelBtnNavigatesToYourCartPage(self):
        title='Verify that clicking on the "Cancel" button navigates to your cart page'
        #pytest.title = title
        cancelBtn = self.presOfEltByXpath(xpath_cancelBtn)
        cancelBtn.click()
        pageTitle1=self.presOfEltByXpath(xpath_sectionHeading)
        if pageTitle1 is not None:
            try:
                assert pageTitle1.text=="Your Cart"
                ssName = saveSS(self.driver, 'test_clickingOnCancelBtnNavigatesToYourCartPage')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_clickingOnCancelBtnNavigatesToYourCartPage')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_clickingOnCancelBtnNavigatesToYourCartPage')
            pytest.screenshot_name = ssName
            pytest.fail("Your Cart Page not found")
    def test_yourInfoPageHasContinueBtn(self):
        title='Verify that the your information page has "Continue" button'
        #pytest.title = title
        checkoutBtn = self.presOfEltByXpath(xpath_checkoutBtn)
        checkoutBtn.click()
        continueBtn = self.presOfEltByXpath(xpath_continueBtn)
        if continueBtn is not None:
            try:
                assert continueBtn.is_displayed() and continueBtn.is_enabled() and continueBtn.get_attribute("value") == 'Continue'
                ssName = saveSS(self.driver, 'test_yourInfoPageHasContinueBtn')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_yourInfoPageHasContinueBtn')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_yourInfoPageHasContinueBtn')
            pytest.screenshot_name = ssName
            pytest.fail("continueBtn not found")

    def test_clickingOnContinueBtnWithEmptyFieldsProvideError(self):
        title='Verify that clicking on the "Continue" button with empty first name, last name and zip code fields provide error messages'
        #pytest.title = title
        continueBtn = self.presOfEltByXpath(xpath_continueBtn)
        continueBtn.click()
        errorMsgFirstName=self.presOfEltByXpath(xpath_errorMsgFirstName)
        if errorMsgFirstName is not None:
            try:
                assert errorMsgFirstName.text=="Error: First Name is required"
                ssName = saveSS(self.driver, 'test_clickingOnContinueBtnWithEmptyFieldsProvideError')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_clickingOnContinueBtnWithEmptyFieldsProvideError')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_clickingOnContinueBtnWithEmptyFieldsProvideError')
            pytest.screenshot_name = ssName
            pytest.fail("errorMsgFirstName not found")

    def test_firstNameFieldIsMandatory(self):
        title='Verify that the first name field is mandatory'
        #pytest.title = title
        self.driver.refresh()
        sleep(2)
        lastNameField = self.presOfEltByXpath(xpath_lastNameField).send_keys('Wick')
        zipCodeField = self.presOfEltByXpath(xpath_zipCodeField).send_keys('2255')
        continueBtn = self.presOfEltByXpath(xpath_continueBtn).click()
        errorMsgFirstName = self.presOfEltByXpath(xpath_errorMsgFirstName)
        if errorMsgFirstName is not None:
            try:
                assert errorMsgFirstName.text == "Error: First Name is required"
                ssName = saveSS(self.driver, 'test_firstNameFieldIsMandatory')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_firstNameFieldIsMandatory')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_firstNameFieldIsMandatory')
            pytest.screenshot_name = ssName
            pytest.fail("errorMsgFirstName not found")

    def test_lastNameFieldIsMandatory(self):
        title='Verify that the last name field is mandatory'
        #pytest.title = title
        self.driver.refresh()
        sleep(2)
        firstNameField=self.presOfEltByXpath(xpath_firstNameField).send_keys('John')
        zipCodeField = self.presOfEltByXpath(xpath_zipCodeField).send_keys('2255')
        continueBtn = self.presOfEltByXpath(xpath_continueBtn).click()
        errorMsgLastName = self.presOfEltByXpath(xpath_errorMsgLastName)
        if errorMsgLastName is not None:
            try:
                assert errorMsgLastName.text == "Error: Last Name is required"
                ssName = saveSS(self.driver, 'test_lastNameFieldIsMandatory')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_lastNameFieldIsMandatory')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_lastNameFieldIsMandatory')
            pytest.screenshot_name = ssName
            pytest.fail("errorMsgLastName not found")
    def test_zipCodeFieldIsMandatory(self):
        title='Verify that the zip code field is mandatory'
        #pytest.title = title
        self.driver.refresh()
        sleep(2)
        firstNameField=self.presOfEltByXpath(xpath_firstNameField).send_keys('John')
        lastNameField = self.presOfEltByXpath(xpath_lastNameField).send_keys('Wick')
        continueBtn = self.presOfEltByXpath(xpath_continueBtn).click()
        errorMsgZipCodeField = self.presOfEltByXpath(xpath_errorMsgZipCodeField)
        if errorMsgZipCodeField is not None:
            try:
                assert errorMsgZipCodeField.text == "Error: Postal Code is required"
                ssName = saveSS(self.driver, 'test_zipCodeFieldIsMandatory')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_zipCodeFieldIsMandatory')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_zipCodeFieldIsMandatory')
            pytest.screenshot_name = ssName
            pytest.fail("errorMsgZipCodeField not found")

    def test_successfulClickOnContinueBtnNavigatesToCheckoutOverviewPage(self):
        title='Verify that a successful click on the continue button navigates to the checkout overview page'
        #pytest.title = title
        self.driver.refresh()
        sleep(2)
        firstNameField = self.presOfEltByXpath(xpath_firstNameField).send_keys('John')
        lastNameField = self.presOfEltByXpath(xpath_lastNameField).send_keys('Wick')
        zipCodeField = self.presOfEltByXpath(xpath_zipCodeField).send_keys('2255')
        continueBtn = self.presOfEltByXpath(xpath_continueBtn).click()
        pageTitle1=self.presOfEltByXpath(xpath_sectionHeading)
        if pageTitle1 is not None:
            try:
                assert pageTitle1.text=="Checkout: Overview"
                ssName = saveSS(self.driver, 'test_successfulClickOnContinueBtnNavigatesToCheckoutOverviewPage')
                pytest.screenshot_name = ssName
            except AssertionError as e:
                ssName = saveSS(self.driver, 'test_successfulClickOnContinueBtnNavigatesToCheckoutOverviewPage')
                pytest.screenshot_name = ssName
                raise
        else:
            ssName = saveSS(self.driver, 'test_successfulClickOnContinueBtnNavigatesToCheckoutOverviewPage')
            pytest.screenshot_name = ssName
            pytest.fail("Checkout Overview page not found")
















