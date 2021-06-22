from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

LOGIN_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/form/button'
LIST_OF_CUSTOMER_XPATH = '//body/div[1]/div/div[2]/div/form/div/select'
NAME_OF_THE_BANK = 'XYZ Bank'

"""Class for the Customer page with methods which using for testing"""

class CustomerPage(BasePage):

    def pick_germiona_accaount(self):
        self.click_on_element_by_xpath('//*[@id="userSelect"]/option[2]')

    def exist_login_button(self):
        try:
            self.find_element_by_xpath(LOGIN_BUTTON_XPATH)
            return True
        except:
            return False

    def exist_list_of_customers(self):
        try:
            self.find_element_by_xpath(LIST_OF_CUSTOMER_XPATH)
            return True
        except:
            return False