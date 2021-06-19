from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

"""Xpaths for the home page"""
HOME_BUTTON_XPATH = "//body/div[1]/div/div[1]/button[1]"
# PROFILE_ICON_XPATH = '//body/div/header/div/div/div/button'
# LOG_OUT_BUTTON_XPATH = '//body/div[2]/div[2]/ul/li'
# SIGN_IN_BUTTON_XPATH = '//body/div/header/div/div/div/a[1]'
# SIGN_UP_BUTTON_XPATH = '//body/div/header/div/div/div/a[2]/span[1]'
# EASY_REST_BUTTON_XPATH = '//header/div/a'
# MODERATOR_PANEL_XPATH = '//body/div[2]/div[2]/ul/a[@href="/moderator"]'
# ADMIN_PANEL_XPATH = '//body/div[2]/div[2]/ul/a[@href="/admin"]'
# ADMINISTRATOR_PANEL_XPATH = '//body/div[2]/div[2]/ul/a[@href="/administrator-panel"]'
# WAITER_PANEL_XPATH = '//body/div[2]/div[2]/ul/a[@href="/waiter"]'
# MY_PROFILE_BUTTON_XPATH = '//body/div[2]/div[2]/ul/a[@href="/profile/personal_info"]'
# MY_RESTAURANTS_BUTTON_XPATH = '//body/div[2]/div[2]/ul/a[@href="/profile/restaurants"]'
# RESTAURANTS_LIST_BUTTON_XPATH = '//header/div/nav/a[2]/span'
# VIEW_ALL_BUTTON_XPATH = '//*[@id="root"]/main/div/div/div[1]/a/img'

"""Class for the Home page with methods which using for testing"""


class HomePage(BasePage):

    def go_to_home_page(self):
        """Method for redirecting on the home page"""
        self.driver.get(base_page.BASE_URL)

    def click_on_home_button(self):
        self.click_on_element_by_xpath(HOME_BUTTON_XPATH)

