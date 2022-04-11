from pyrsistent import b
from selenium.webdriver.common.by import By

class Locators:
    
    '''Loginpage'''
    LOGIN_PAGE_TITLE = (By.XPATH, "//*[text()='Swag Labs']")
    EMAIL = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Epic sadface: Username and password do not match any user in this service']")

    '''Homepage'''
    HOME_PAGE_TITLE = (By.XPATH, "//*[text()='Swag Labs']")
    PRODUCT_SORT_CONTAINER = (By.XPATH, "//*[@class='product_sort_container']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    HEADER = (By.XPATH, "//span[text()='Products']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')])[%s]")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    '''Cart page'''
    CART_PAGE_HEADER = (By.XPATH, "//span[text()='Your Cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")

    '''CHECKOUT: YOUR INFORMATION'''
    CHECKOUT_YOUR_INFO_PAGE_HEADER = (By.XPATH, "//*[text()='Checkout: Your Information']")
    FIRST_NAME = (By.XPATH, "(//*[@class='input_error form_input'])[1]")
    LAST_NAME = (By.XPATH, "(//*[@class='input_error form_input'])[2]")
    ZIP_POSTAL_CODE = (By.XPATH, "(//*[@class='input_error form_input'])[3]")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='continue']")

    '''Checkout overview page'''
    CHECKOUT_OVERVIEW_PAGE_HEADER = (By.XPATH, "//*[text()='Checkout: Overview']")
    FINISH_BUTTON = (By.XPATH, "//button[text()='Finish']")

    '''Checkout complete page'''
    CHECKOUT_COMPLETE_PAGE = (By.XPATH, "//span[text()='Checkout: Complete!']")
    CHECKOUT_COMPLETE_PAGE_HEADER = (By.XPATH, "//h2[text()='THANK YOU FOR YOUR ORDER']")
    CHECKOUT_COMPLETE_PAGE_ORDER_MESSAGE = (By.XPATH, "//*[contains(text(),'Your order has been dispatched')]")
    CHECKOUT_COMPLETE_PAGE_IMAGE = (By.XPATH, "//*[@alt='Pony Express']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[@id='back-to-products']")