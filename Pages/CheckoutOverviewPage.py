import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Products


class CheckoutOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def  checkout_overview_page_header(self):
        return self.get_element_text(Locators.CHECKOUT_OVERVIEW_PAGE_HEADER)

    def is_items_getting_displayed_in_cart(self):
        items = []
        for getValue in Products:
            searchIconPresence  = self.driver.find_element_by_xpath(
                 "//div[contains(text(),'%s')]" % str(getValue.value)) 
            items.append(searchIconPresence.text)
            print(items)
        assert searchIconPresence.text == getValue.value

    def do_click_on_finish_button(self):
        self.do_click(Locators.FINISH_BUTTON)