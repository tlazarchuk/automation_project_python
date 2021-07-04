import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

"""URLs used when testing log-in functionality"""
BASE_URL = os.getenv('TEST_BASE_URL', 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#')
LOGIN_URL = '{}/login'.format(BASE_URL)
CUSTOMER_URL = '{}/customer'.format(BASE_URL)
MANAGER_URL = '{}/manager'.format(BASE_URL)
ADD_CUSTOMER_URL = '{}/manager/addCust'.format(BASE_URL)
OPEN_ACCOUNT_URL = '{}/manager/openAccount'.format(BASE_URL)
CUSTOMERS_URL = '{}/manager/list'.format(BASE_URL)
ACCOUNT_URL = '{}/account'.format(BASE_URL)
TRANSACTION_URL = '{}/listTx'.format(BASE_URL)

"""Base Page, parent class for other pages"""


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
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
