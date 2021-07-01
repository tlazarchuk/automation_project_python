import unittest
import time

from selenium import webdriver

from pages import base_page as bp
from pages import home_page as hp
from pages import customer_page as cp
from pages import manager_page as mp
from pages import account_page as ap

class CorrectnessUrlManagerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.base_page = bp.BasePage(self.driver)
        self.customer_page = cp.CustomerPage(self.driver)
        self.manager_page = mp.ManagerPage(self.driver)
        self.account_page = ap.AccountPage(self.driver)
        self.home_page.go_to_home_page()
        self.home_page.click_on_custom_login_button()
        self.customer_page.pick_germiona_account()
        self.customer_page.click_on_login_button()

    def tearDown(self):
        self.driver.quit()

    # def test_check_logout_button(self): 
    #     self.account_page.click_logout_button()
    #     self.base_page.wait_for_url(bp.CUSTOMER_URL)
    #     current_url = self.driver.current_url
    #     self.assertEqual(current_url, bp.CUSTOMER_URL)

    # def test_check_transaction_button(self): 
    #     self.account_page.click_on_transaction_button()
    #     self.base_page.wait_for_url(bp.TRANSACTION_URL)
    #     current_url = self.driver.current_url
    #     self.assertEqual(current_url, bp.TRANSACTION_URL)

    def test_make_deposit(self):
        current_money = self.account_page.get_money_balance() 
        self.account_page.click_on_deposit_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        current_money += 300
        balance_money = self.account_page.get_money_balance()
        self.assertEqual(current_money, balance_money)
        time.sleep(2)

    def test_make_withdrawl(self):
        current_money = self.account_page.get_money_balance() 
        self.account_page.click_on_withdrawl_button()
        self.account_page.fill_currency_for_deposit_or_withdrawl(300)
        self.account_page.click_on_confirm_button()
        current_money -= 300
        balance_money = self.account_page.get_money_balance()
        self.assertEqual(current_money, balance_money)
        time.sleep(2)


if __name__ == "__main__":
  unittest.main()
