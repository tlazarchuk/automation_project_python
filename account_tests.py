import unittest

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp
from pages import customer_page as cp
from pages import account_page as ap

class HOmePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.account_page = ap.AccountPage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
  unittest.main()
