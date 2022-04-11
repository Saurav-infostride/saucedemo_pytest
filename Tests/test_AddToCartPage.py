import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Pages.AddToCartPage import AddToCartPage
from Locators.Locators import Locators
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage

class Test_AddTOCartPage(BaseTest):
    
    @pytest.mark.order()
    def test_verify_cart_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_click(Locators.CART_ICON)
        addToCartPage = homePage
        cart_title = addToCartPage.get_element_text(Locators.CART_PAGE_HEADER)
        assert cart_title == TestData.CART_PAGE_HEADER
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''correct_1'''
    @pytest.mark.order()
    def test_verify_item_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.is_items_exist_in_cart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
