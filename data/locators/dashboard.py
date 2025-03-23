
elements=dict(
    pageTitle='Swag Labs',
    sectionHeading='Products'
)

ids=dict(
    logoutLink="logout_sidebar_link"
)

xpaths=dict(
    hamburgerBtn="//button[@id='react-burger-menu-btn']",
    title="//span[@class='title']",
    pageLogo="//div[@class='app_logo']",
    sectionHeading="//span[@class='title']",
    sortContainer="//select[@class='product_sort_container']",
    s0="//option[@value='az']",
    s1="//option[@value='za']",
    s2="//option[@value='lohi']",
    s3="//option[@value='hilo']",
    backpackImg="//img[@alt='Sauce Labs Backpack']",
    backpackProdName="//div[normalize-space()='Sauce Labs Backpack']",
    backpackProdPrice="//div[@class='inventory_list']//div[1]//div[2]//div[2]//div[1]",
    backpackAddToCartBtn="//button[@id='add-to-cart-sauce-labs-backpack']",
    backpackRemoveBtn="//button[@id='remove-sauce-labs-backpack']",
    cartBadge="//span[@class='shopping_cart_badge']",
    bikeLightImg="//img[@alt='Sauce Labs Bike Light']",
    bikeLightName="//div[normalize-space()='Sauce Labs Bike Light']",
    bikeLightPrice="//div[@id='inventory_container']//div[2]//div[2]//div[2]//div[1]",
    bikeLightAddToCart="//button[@id='add-to-cart-sauce-labs-bike-light']",
    shoppingCartLink="//a[@class='shopping_cart_link']",
    bikeLightAddToCartBtn="//button[@id='add-to-cart-sauce-labs-bike-light']",
    bikeLightRemoveBtn="//button[@id='remove-sauce-labs-bike-light']",
    tShirtImg="//img[@alt='Sauce Labs Bolt T-Shirt']",
    tShirtName="//div[normalize-space()='Sauce Labs Bolt T-Shirt']",
    tShirtPrice="//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div",
    tShirtAddToCart="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
    tShirtRemoveBtn="//button[@id='remove-sauce-labs-bolt-t-shirt']",
    onesieImg="//img[@alt='Sauce Labs Onesie']",
    onesieName="//div[normalize-space()='Sauce Labs Onesie']",
    onesiePrice='//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div',
    onesieAddToCart="//button[@id='add-to-cart-sauce-labs-onesie']",
    onesieRemoveBtn="//button[@id='remove-sauce-labs-onesie']",
    cartIcon="//a[@class='shopping_cart_link']",
    yourCartPageTitle="//span[@class='title']",
    priceOfBackPackInCart='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
    priceOfBikeLightInCart='//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div',
    priceOfTshirtInCart='//*[@id="cart_contents_container"]/div/div[1]/div[5]/div[2]/div[2]/div',
    priceOfOnesieInCart='//*[@id="cart_contents_container"]/div/div[1]/div[6]/div[2]/div[2]/div',
    continueShoppingBtn="//button[@id='continue-shopping']",
    checkoutBtn="//button[@id='checkout']",
    firstNameField="//input[@id='first-name']",
    lastNameField="//input[@id='last-name']",
    zipCodeField="//input[@id='postal-code']",
    cancelBtn="//button[@id='cancel']",
    continueBtn="//input[@id='continue']",
    errorMsgFirstName="//h3[normalize-space()='Error: First Name is required']",
    errorMsgLastName="//h3[normalize-space()='Error: Last Name is required']",
    errorMsgZipCodeField="//h3[normalize-space()='Error: Postal Code is required']"
)

className=dict(
    productNameClass='inventory_item_name ',
    productPriceClass='inventory_item_price',
    yourCartItemNamesClass='inventory_item_name',
    yourCartItemPricesClass='inventory_item_price'
)

sortOrders=dict(
    s0='Name (A to Z)',
    s1='Name (Z to A)',
    s2='Price (low to high)',
    s3='Price (high to low)',
)