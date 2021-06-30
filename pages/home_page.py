from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

"""Xpaths for the home page"""
HOME_BUTTON_XPATH = '//body/div[1]/div/div[1]/button[1]'
CUSTOM_LOGIN_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/div[1]/button'
BANK_MANAGER_LOGIN_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/div[2]/button'
NAME_OF_THE_BANK_XPATH = '/html/body/div[1]/div/div[1]/strong'

"""Class for the Home page with methods which using for testing"""
NAME_OF_THE_BANK = 'XYZ Bank'

class HomePage(BasePage):

    def go_to_home_page(self):
        """Method for redirecting on the home page"""
        self.driver.get(base_page.LOGIN_URL)

    def click_on_home_button(self):
        self.click_on_element_by_xpath(HOME_BUTTON_XPATH)

    def click_on_custom_login_button(self):
        self.click_on_element_by_xpath(CUSTOM_LOGIN_BUTTON_XPATH)

    def click_on_bank_manager_login_button(self):
        self.click_on_element_by_xpath(BANK_MANAGER_LOGIN_BUTTON_XPATH)

    def get_name_of_the_bank(self):
        return self.find_element_by_xpath(NAME_OF_THE_BANK_XPATH).text

    def get_title(self):
        return self.driver.title

    def click_on_custom_login_button(self):
        self.click_on_element_by_xpath(CUSTOM_LOGIN_BUTTON_XPATH)

    def click_on_bank_manager_login_button(self):
        self.click_on_element_by_xpath(BANK_MANAGER_LOGIN_BUTTON_XPATH)

    def go_to_add_customer(self):
        self.go_to_home_page()
        self.driver.implicitly_wait(30)
        self.click_on_bank_manager_login_button()
