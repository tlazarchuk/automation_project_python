import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import base_page as bp
from pages import home_page as hp
from pages import customer_page as cp
from pages import manager_page as mp

class HOmePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.manager_page = mp.ManagerPage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_add_customer(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.fill_first_name_for_test('Alberto')
        self.manager_page.fill_last_name_for_test('Del Rio')
        self.manager_page.fill_post_code_for_test('E100000')
        self.manager_page.click_on_create_customer_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()


if __name__ == "__main__":
  unittest.main()
  