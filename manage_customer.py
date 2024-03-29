import unittest

from selenium import webdriver

from pages import home_page as hp
from pages import customer_page as cp
from pages import manager_page as mp

class ManageCustomerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.manager_page = mp.ManagerPage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)
        self.home_page.click_on_bank_manager_login_button()
        self.manager_page.create_test_customer()

    def tearDown(self):
        self.driver.quit()

    def test_delete_customer(self):
        self.manager_page.click_on_customers_button()
        self.manager_page.fill_search_input_using_name('Alberto')
        self.manager_page.delete_customer_when_search()
        self.manager_page.clear_search_input()
        boolearn = self.manager_page.if_customer_exist('Alberto')
        self.assertFalse(boolearn)

    def test_search_customer(self):
        self.manager_page.click_on_customers_button()
        boolearn = self.manager_page.if_customer_exist('Alberto')
        self.assertTrue(boolearn)
    
if __name__ == "__main__":
  unittest.main()
  