import unittest

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp
from pages import customer_page as cp

class HOmePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_appear_button_login(self):
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_germiona_accaount()
        boolean = self.customer_page.exist_login_button()
        self.assertTrue(boolean)

    def test_appear_list_of_customers(self):
        self.home_page.click_on_custom_login_button()
        boolean = self.customer_page.exist_list_of_customers()
        self.assertTrue(boolean)

if __name__ == "__main__":
  unittest.main()
  