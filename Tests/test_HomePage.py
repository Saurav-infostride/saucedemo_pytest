import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from EnumsPackage.Enums import Sort_Productss

class Test_Home(BaseTest):
    
    '''Title'''
    @pytest.mark.order()
    def test_verify_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        title = homePage.get_title()
        assert title == TestData.HOME_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''Header'''
    @pytest.mark.order()
    def test_verify_home_page_header(self): 
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        header = homePage.get_header_value()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)
        assert header == TestData.HOME_PAGE_HEADER

    '''Cart Icon'''
    @pytest.mark.order()
    def test_verify_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        notification = homePage.is_cart_icon_exist()
        assert notification
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

    '''asserting products sort container'''
    @pytest.mark.order()
    def test_verify_product_sort_container(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.product_sort_container()
        for getValue in Sort_Productss:
            sortingNames  = self.driver.find_element_by_xpath(
                     "//*[@class='product_sort_container']//option[contains(text(),'%s')]" % str(getValue.value)) 
            print(sortingNames)
            assert sortingNames.text == getValue.value

    '''Shopping functionality'''
    @pytest.mark.order()
    def test_verify_shopping(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_shopping()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''Sorting products in Low to High range'''
    @pytest.mark.order()
    def test_verify_sorting_L_to_H(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.product_sort_container_low_to_high()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''Sorting products in High to Low range'''
    @pytest.mark.order()
    def test_verify_sorting_H_to_L(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.product_sort_container_High_to_Low()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''Sorting products in Z to A name'''
    @pytest.mark.order()
    def test_verify_sorting_Z_To_A(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.sort_products_by_Z_To_A()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''Sorting products in Z to A name'''
    @pytest.mark.order()
    def test_verify_sorting_A_To_Z(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.sort_products_by_A_To_Z()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
        
    '''Logout'''
    @pytest.mark.order()
    def test_verify_logout_into_app(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_logout()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)