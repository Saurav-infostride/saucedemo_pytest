import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Products


class CheckoutCompletePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def checkout_complete_page_header(self):
        return self.get_element_text(Locators.CHECKOUT_COMPLETE_PAGE_HEADER)

    def checkout_complete_page_order_message(self):
        return self.get_element_text(Locators.CHECKOUT_COMPLETE_PAGE_ORDER_MESSAGE)

    def checkout_complete_page_order_back_home_button(self):
        self.do_click(Locators.BACK_HOME_BUTTON)