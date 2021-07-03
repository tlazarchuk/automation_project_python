import unittest

from selenium import webdriver

from pages import home_page as hp
from pages import customer_page as cp
from pages import manager_page as mp
from pages import account_page as ap

class CorrectnessUrlManagerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.manager_page = mp.ManagerPage(self.driver)
        self.account_page = ap.AccountPage(self.driver)
        self.home_page.go_to_add_customer()
        self.manager_page.create_test_customer()
        self.manager_page.click_on_open_accaunt_button()
        self.manager_page.select_customer_in_list()

    def tearDown(self):
        self.driver.quit()

    def test_check_welcome_text(self):
        self.manager_page.accept_popup()
        self.home_page.click_on_home_button()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_test_account()
        self.customer_page.click_on_login_button()
        current_text = self.account_page.get_welcome_text()
        needed_text = self.account_page.return_needed_welcome_text()
        self.assertEqual(current_text, needed_text)

    def test_check_currency(self):
        self.manager_page.accept_popup()
        self.home_page.click_on_home_button()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_test_account()
        self.customer_page.click_on_login_button()
        current_currency = self.account_page.get_currency_text()
        needed_currency = self.account_page.return_needed_currency_text()
        self.assertEqual(current_currency, needed_currency)

    def test_check_account_number(self):
        account_number = self.manager_page.get_response_from_popup_account_number()
        self.manager_page.accept_popup()
        self.home_page.click_on_home_button()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_test_account()
        self.customer_page.click_on_login_button()
        current_account_number = self.account_page.get_account_number()
        self.assertEqual(current_account_number, account_number)

    def test_check_money_balance(self):
        self.manager_page.accept_popup()
        self.home_page.click_on_home_button()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_test_account()
        self.customer_page.click_on_login_button()
        current_money_balance = self.account_page.get_money_balance()
        self.assertEqual(current_money_balance, 0)

    def test_check_if_actions_buttons_appear(self):
        self.manager_page.accept_popup()
        self.home_page.click_on_home_button()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_test_account()
        self.customer_page.click_on_login_button()
        boolearn = self.account_page.if_actions_buttons_exist()
        self.assertTrue(boolearn)

if __name__ == "__main__":
  unittest.main()
