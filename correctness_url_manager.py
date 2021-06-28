import unittest

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp
from pages import customer_page as cp
from pages import manager_page as mp

class CorrectnessUrlManagerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.manager_page = mp.ManagerPage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)
        self.home_page.click_on_bank_manager_login_button()

    def tearDown(self):
        self.driver.quit()

    def test_url_add_customer(self):
        self.manager_page.click_on_add_customer_button()
        self.base_page.wait_for_url(bp.ADD_CUSTOMER_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.ADD_CUSTOMER_URL)

    def test_url_open_account(self):
        self.manager_page.click_on_open_accaunt_button()
        self.base_page.wait_for_url(bp.OPEN_ACCOUNT_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.OPEN_ACCOUNT_URL)

    def test_url_customers(self):
        self.manager_page.click_on_customers_button()
        self.base_page.wait_for_url(bp.CUSTOMERS_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.CUSTOMERS_URL)


if __name__ == "__main__":
  unittest.main()
