import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

"""URLs used when testing log-in functionality"""
BASE_URL = os.getenv('TEST_BASE_URL', 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
LOGIN_PAGE_URL = '{}/log-in'.format(BASE_URL)
RESTAURANT_LIST_URL = '{}/restaurants'.format(BASE_URL)
MODERATOR_PANEL_URL = '{}/moderator'.format(BASE_URL)
ADMIN_PANEL_URL = '{}/admin'.format(BASE_URL)
ADMINISTRATOR_PANEL_URL = '{}/administrator-panel'.format(BASE_URL)
WAITER_PANEL_URL = '{}waiter/orders'.format(BASE_URL)
SIGNUP_PAGE_URL = '{}/sign-up'.format(BASE_URL)
MODERATOR_RESTAURANTS_URL = '{}/moderator/restaurants'.format(BASE_URL)
MODERATOR_USERS_URL = '{}/moderator/users'.format(BASE_URL)
MODERATOR_OWNERS_URL = '{}/moderator/owners'.format(BASE_URL)
OWNER_MY_RESTAURANTS_URL = '{}/profile/restaurants'.format(BASE_URL)
PROFILE_PAGE_URL = '{}/profile'.format(BASE_URL)

"""Base Page, parent class for other pages"""


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 10)        # default
        self.wait = WebDriverWait(self.driver, 20)

    def find_element_by_xpath(self, element_xpath):
        """Method for finding element on the page"""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    def click_on_element_by_xpath(self, element_xpath):
        """Method for clicking on the element"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()

    def clear_text_field_by_xpath(self, element_xpath):
        """Method for clearing the text field"""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath))).clear()

    def fill_in_text_field_by_xpath(self, element_xpath, text):
        """Method for filling in the text field with text"""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath))).send_keys(text)
        
    def wait_invisibility_of_element(self, element_xpath):
        """Method for waiting until the element gets invisibility or disappears from the DOM"""
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, element_xpath)))

    def wait_for_url(self, element_url):
        """Method for waiting for url to be as parameter what it takes (element-url)"""
        self.wait.until(EC.url_to_be(element_url))

    def url_to_be(self, URL):
        return EC.url_to_be(URL)
