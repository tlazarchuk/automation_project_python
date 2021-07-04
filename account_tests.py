import unittest
import time

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp
from pages import customer_page as cp
from pages import account_page as ap
from pages import transaction_page as tp

class CorrectnessUrlManagerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.account_page = ap.AccountPage(self.driver)
        self.transaction_page = tp.TransactionPage(self.driver)
        self.home_page.go_to_home_page()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_germiona_account()
        self.customer_page.click_on_login_button()

    def tearDown(self):
        self.driver.quit()

    def test_check_logout_button(self): 
        self.account_page.click_logout_button()
        self.base_page.wait_for_url(bp.CUSTOMER_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.CUSTOMER_URL)

    def test_check_transaction_button(self): 
        self.account_page.click_on_transaction_button()
        self.base_page.wait_for_url(bp.TRANSACTION_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.TRANSACTION_URL)

    def test_make_deposit(self):
        current_money = self.account_page.get_money_balance() 
        self.account_page.click_on_deposit_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        current_money += 300
        balance_money = self.account_page.get_money_balance()
        self.assertEqual(current_money, balance_money)

    def test_make_withdrawl(self):
        current_money = self.account_page.get_money_balance() 
        self.account_page.click_on_withdrawl_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        current_money -= 300
        balance_money = self.account_page.get_money_balance()
        self.assertEqual(current_money, balance_money)

    def test_make_withdrawl_all(self):
        current_money = self.account_page.get_money_balance() 
        self.account_page.click_on_withdrawl_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(int(current_money))
        self.account_page.click_on_confirm_button()
        current_money = 0
        balance_money = self.account_page.get_money_balance()
        self.assertEqual(current_money, balance_money)

    def test_make_withdrawl_more_than_balance(self):
        current_money = self.account_page.get_money_balance() 
        self.account_page.click_on_withdrawl_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(int(current_money)+1)
        self.account_page.click_on_confirm_button()
        balance_money = self.account_page.get_money_balance()
        self.assertEqual(current_money, balance_money)

    def test_back_button(self):
        self.account_page.click_on_transaction_button()
        self.transaction_page.click_on_back_button()
        self.base_page.wait_for_url(bp.ACCOUNT_URL)
        current_url = self.driver.current_url
        self.assertEqual(current_url, bp.ACCOUNT_URL)

    def test_transaction_history_first(self):
        self.account_page.click_on_transaction_button()
        self.transaction_page.click_on_reset_button()
        self.transaction_page.click_on_back_button()
        self.account_page.click_on_deposit_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        self.account_page.click_on_transaction_button()
        transaction_type = self.transaction_page.get_first_in_list_transaction_type()
        self.assertEqual(transaction_type, 'Credit')

    def test_transaction_history_second(self):
        self.account_page.click_on_transaction_button()
        self.transaction_page.click_on_reset_button()
        self.transaction_page.click_on_back_button()
        self.account_page.click_on_deposit_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        self.account_page.click_on_withdrawl_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        self.account_page.click_on_transaction_button()
        transaction_type = self.transaction_page.get_second_in_list_transaction_type()
        self.assertEqual(transaction_type, 'Debit')

    def test_reset_button(self):
        self.account_page.click_on_transaction_button()
        self.transaction_page.click_on_reset_button()
        self.transaction_page.click_on_back_button()
        self.account_page.click_on_deposit_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        self.account_page.click_on_transaction_button()
        self.transaction_page.click_on_reset_button()
        boolearn = self.transaction_page.find_first_in_list_transaction_type()
        self.assertFalse(boolearn)

    def test_change_account_number(self):
        self.account_page.click_on_account_number_1002()
        account_number = self.account_page.get_account_number()
        self.assertEqual('1002', account_number)

if __name__ == "__main__":
  unittest.main()
