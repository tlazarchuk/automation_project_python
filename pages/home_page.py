from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

"""Xpaths for the home page"""
HOME_BUTTON_XPATH = '//body/div[1]/div/div[1]/button[1]'
CUSTOM_LOGIN_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/div[1]/button'
BANK_MANAGER_LOGIN_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/div[2]/button'

"""Class for the Home page with methods which using for testing"""


class HomePage(BasePage):

    def go_to_home_page(self):
        """Method for redirecting on the home page"""
        self.driver.get(base_page.BASE_URL)

    def click_on_home_button(self):
        self.click_on_element_by_xpath(HOME_BUTTON_XPATH)

    def click_on_custom_login_button(self):
        self.click_on_element_by_xpath(CUSTOM_LOGIN_BUTTON_XPATH)

    def click_on_bank_manager_login_button(self):
        self.click_on_element_by_xpath(BANK_MANAGER_LOGIN_BUTTON_XPATH)
