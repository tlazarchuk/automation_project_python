import unittest
import time

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp

class GotoHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_check_home_page_url(self):
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.BASE_URL)

    def test_check_home_button(self):
        self.home_page.click_on_home_button()
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.BASE_URL)

    def test_check_custom_login_button(self):
        self.home_page.click_on_custom_login_button()
        self.base_page.wait_for_url(bp.CUSTOMER_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.CUSTOMER_URL)

    def test_check_bank_manager_login_button(self):
        self.home_page.click_on_bank_manager_login_button()
        self.base_page.wait_for_url(bp.MANAGER_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.MANAGER_URL)

if __name__ == "__main__":
  unittest.main()