import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
from Pages.AddToCartPage import AddToCartPage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Locators.Locators import Locators

class Test_CheckoutYourInfoPage(BaseTest):

    @pytest.mark.order()
    def test_verify_checkout_your_info_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        self.homePage = HomePage(self.driver)
        homePage.do_shopping()
        self.addToCart = AddToCartPage(self.driver)
        self.addToCart.do_click_checkout_button()
        self.checkInfo = CheckoutYourInfoPage(self.driver)
        title = self.checkInfo.get_element_text(Locators.CHECKOUT_YOUR_INFO_PAGE_HEADER)
        assert title == TestData.CHECKOUT_YOUR_INFO_HEADER
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)  

    @pytest.mark.order()
    def test_verify_enter_info_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        self.homePage = HomePage(self.driver)
        homePage.do_shopping()
        self.addToCart = AddToCartPage(self.driver)
        self.addToCart.do_click_checkout_button()
        self.checkInfo = CheckoutYourInfoPage(self.driver)
        self.checkInfo.do_enter_your_info()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)      
