import unittest

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp

class HOmePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)

    def tearDown(self):
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

    def test_check_name_of_the_bank(self):
        name_of_the_bank = self.home_page.get_name_of_the_bank()
        self.assertEqual(name_of_the_bank, hp.NAME_OF_THE_BANK)

    def test_check_title(self):
        title = self.home_page.get_title()
        self.assertEqual(title, hp.NAME_OF_THE_BANK)

if __name__ == "__main__":
  unittest.main()
