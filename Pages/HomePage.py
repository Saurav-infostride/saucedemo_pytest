
import os,sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Products, Products_Z_To_A, Sort_Products

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''Title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    '''To check Cart icon'''
    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

    '''To get header text'''
    def get_header_value(self):
        return self.get_element_text(Locators.HEADER)

    '''Product sorting container functionality'''
    def product_sort_container(self):
        for i in Sort_Products:
            b = self.driver.find_element_by_xpath(
                "(//*[@class='product_sort_container']//option)[%s]" % str(i.value))
            b.click()

    '''To sort products in low to high range'''
    def product_sort_container_low_to_high(self):
        b = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.PRICE_LOW_TO_HIGH.value))
        b.click()
        a = []
        all_spans = self.driver.find_elements_by_class_name("inventory_item_price")
        for span in all_spans:
            a.append(span.text.replace("$",""))
            print(a)
        assert a[0]<a[1], "products are not sorted"

    '''To sort products in high to low range'''
    def product_sort_container_High_to_Low(self):
        c = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.PRICE_HIGH_TO_LOW.value))
        c.click()
        des = []
        all_spans = self.driver.find_elements_by_class_name("inventory_item_price")
        for span in all_spans:
            des.append(float(span.text.replace("$","")))
            print(des)
        total = 0
        for ele in range(0,len(des)):
            total = total + des[ele]
            print(total)
        assert des[0]>des[1], "products are not sorted"
    
    '''To sort products in Z to A name range'''
    def sort_products_by_Z_To_A(self):
        d = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.NAME_Z_A.value))
        d.click()
        feg = []
        for getValue in Products_Z_To_A:
            sortingNames  = self.driver.find_element_by_xpath(
                     "//*[contains(text(),'%s')]" % str(getValue.value)) 
            feg.append(sortingNames.text)
            print(feg)
            assert sortingNames.text == getValue.value 

    '''To sort products in Z to A name range'''
    def sort_products_by_A_To_Z(self):
        d = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.NAME_A_TO_Z.value))
        d.click()
        feg = []
        for getValue in Products:
            sortingNames  = self.driver.find_element_by_xpath(
                     "//*[contains(text(),'%s')]" % str(getValue.value)) 
            feg.append(sortingNames.text)
            print(feg)
            assert sortingNames.text == getValue.value 
        
    ''' Add to Cart functionality'''
    def do_shopping(self):
        for i in Products:
            a = self.driver.find_element_by_xpath(
                "//div[contains(text(),'%s')]/following::button" % str(i.value))
            a.click()
        self.do_click(Locators.CART_ICON)

    '''Logout'''
    def do_logout(self):
        self.do_click(Locators.BURGER_MENU_BUTTON)
        self.do_click(Locators.LOGOUT_BUTTON)
