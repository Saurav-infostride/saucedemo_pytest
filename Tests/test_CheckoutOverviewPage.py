import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
import time
from Pages.AddToCartPage import AddToCartPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Locators.Locators import Locators
from Config.config import TestData


class Test_CheckoutOverviewPage(BaseTest):

    @pytest.mark.order()
    def test_verify_checkout_overview_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        self.homePage = HomePage(self.driver)
        homePage.do_shopping()
        self.addToCart = AddToCartPage(self.driver)
        self.addToCart.do_click_checkout_button()
        self.checkInfo = CheckoutYourInfoPage(self.driver)
        self.checkInfo.do_enter_your_info()  
        self.checkoutOverview = CheckoutOverviewPage(self.driver)
        checkout_overview_page_header = self.checkoutOverview.get_element_text(Locators.CHECKOUT_OVERVIEW_PAGE_HEADER)
        assert checkout_overview_page_header == TestData.CHECKOUT_OVERVIEW_HEADER
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order()
    def test_verify_click_on_finish_button(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        self.homePage = HomePage(self.driver)
        homePage.do_shopping()
        self.addToCart = AddToCartPage(self.driver)
        self.addToCart.do_click_checkout_button()
        self.checkInfo = CheckoutYourInfoPage(self.driver)
        self.checkInfo.do_enter_your_info()
        self.checkoutOverview = CheckoutOverviewPage(self.driver)
        self.checkoutOverview.is_items_exist_in_cart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)  