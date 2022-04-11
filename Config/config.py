class TestData:
    # CHROME_EXECUTABLE_PATH = "C:\Users\SauravSharma\Drivers\chromedriver.exe"
    # FIREFOX_EXECUTABLE_PATH = "C:\Users\SauravSharma\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe"

    BASE_URL = "https://www.saucedemo.com/"
    '''login page'''
    
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    INC_USERNAME = "Not_the_Standard_user"
    INC_PASSWORD = "INCorRECt_PasSWoRd"
    LOGIN_WITH_INCORRECT_CREDENTIALS_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
    LOGIN_PAGE_TITLE = "Swag Labs"

    '''homepage'''
    HOME_PAGE_TITLE = "Swag Labs"
    HOME_PAGE_HEADER = "PRODUCTS"

    '''cart page'''
    CART_PAGE_HEADER = "YOUR CART"

    '''Check out your Info page'''
    CHECKOUT_YOUR_INFO_HEADER = "CHECKOUT: YOUR INFORMATION"
    FIRST_NAME = "The"
    LAST_NAME = "Rock"
    POSTAL_CODE = 1234

    '''Checkout overview page'''
    CHECKOUT_OVERVIEW_HEADER = "CHECKOUT: OVERVIEW"

    '''Checkout complete page'''
    CHECKOUT_COMPLETE_PAGE_HEADER = "THANK YOU FOR YOUR ORDER"