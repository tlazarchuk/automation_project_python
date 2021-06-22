from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

LOGOUT_BUTTON = '//body/div[1]/div/div[1]/button[2]'

"""Class for the Account page with methods which using for testing"""

class AccountPage(BasePage):

    def click_button_logout(self):
        self.click_on_element_by_xpath(LOGOUT_BUTTON)