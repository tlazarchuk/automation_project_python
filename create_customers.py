import unittest

from selenium import webdriver

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

    def test_add_correct_customer(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('Alberto', 'Del Rio', 'E800000')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertTrue(boolean)

    def test_add_customer_without_name(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('', 'Del Rio', 'E80000')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertTrue(boolean)

    def test_add_customer_without_lastname(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('Albearto', '', 'E80000')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertTrue(boolean)

    def test_add_customer_without_postcode(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('Albearto', 'Del Rio', '')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertTrue(boolean)

    def test_add_customer_with_invalid_name(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('!@#$%^%', 'Del Rio', 'E100000')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertFalse(boolean)

    def test_add_customer_with_invalid_lastname(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('Alberto', '!@@###$$%', 'E100000')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertFalse(boolean)

    def test_add_customer_with_invalid_Postcode(self):
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.click_on_add_customer_button()
        self.manager_page.create_customer_with_filds('Alberto', 'Del Rio', '!@#$%^')
        self.manager_page.click_on_create_customer_button()
        boolean = self.manager_page.if_user_created()
        self.assertFalse(boolean)

if __name__ == "__main__":
  unittest.main()
  