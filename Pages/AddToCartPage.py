import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from EnumsPackage.Enums import Products
from Pages.BasePage import BasePage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage

class AddToCartPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def get_add_to_cart_page_header(self):
            return self.get_element_text(Locators.CART_PAGE_HEADER)

        def is_items_exist_in_cart(self):
            items = []
            for getValue in Products:
                searchIconPresence  = self.driver.find_element_by_xpath(
                     "//div[contains(text(),'%s')]" % str(getValue.value))
                items.append(searchIconPresence.text) 
                print(items)
            assert searchIconPresence.text == getValue.value

        def do_click_checkout_button(self):
            self.do_click(Locators.CHECKOUT_BUTTON)
            return CheckoutYourInfoPage(self.driver)

