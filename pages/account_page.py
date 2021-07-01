from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

LOGOUT_BUTTON_XPATH = '//body/div[1]/div/div[1]/button[2]'
WELCOME_TEXT_XPATH = '//body/div/div/div[2]/div/div[1]/strong'
CURRENCY_TEXT_XPATH = '//body/div/div/div[2]/div/div[2]/strong[3]'
ACCOUNT_NUMBER_XPATH = '//body/div/div/div[2]/div/div[2]/strong[1]'
MONEY_BALANCE_XPATH = '//body/div/div/div[2]/div/div[2]/strong[2]'
ACTIONS_BUTTONS_XPATH = '//body/div/div/div[2]/div/div[3]'
TRANSACTION_BUTTON_XPATH = '//body/div/div/div[2]/div/div[3]/button[1]'
DEPOSIT_BUTTON_XPATH = '//body/div/div/div[2]/div/div[3]/button[2]'
WITHDRAWL_BUTTON_XPATH = '//body/div/div/div[2]/div/div[3]/button[3]'
INPUT_DEPOSIT_OR_WITHDRAWL_XPATH = '//body/div/div/div[2]/div/div[4]/div/form/div/input'
CONFIRM_DEPOSIT_OR_WITHDRAWL_BUTTON_XPATH = '//body/div/div/div[2]/div/div[4]/div/form/button'

"""Class for the Account page with methods which using for testing"""

class AccountPage(BasePage):

    def click_logout_button(self):
        self.click_on_element_by_xpath(LOGOUT_BUTTON_XPATH)

    def get_welcome_text(self):
        return self.find_element_by_xpath(WELCOME_TEXT_XPATH).text

    def return_needed_welcome_text(self):
        return 'Welcome Alberto Del Rio !!'

    def get_currency_text(self):
        return self.find_element_by_xpath(CURRENCY_TEXT_XPATH).text

    def return_needed_currency_text(self):
        return 'Pound'

    def get_account_number(self):
        return self.find_element_by_xpath(ACCOUNT_NUMBER_XPATH).text

    def get_money_balance(self):
        return int(self.find_element_by_xpath(MONEY_BALANCE_XPATH).text)

    def if_actions_buttons_exist(self):
        try:
            self.click_on_element_by_xpath(ACTIONS_BUTTONS_XPATH)
            return True
        except:
            return False

    def click_on_transaction_button(self):
        self.click_on_element_by_xpath(TRANSACTION_BUTTON_XPATH)

    def click_on_deposit_button(self):
        self.click_on_element_by_xpath(DEPOSIT_BUTTON_XPATH)

    def click_on_withdrawl_button(self):
        self.click_on_element_by_xpath(WITHDRAWL_BUTTON_XPATH)

    def fill_currency_for_deposit_or_withdrawl(self, currency):
        self.fill_in_text_field_by_xpath(INPUT_DEPOSIT_OR_WITHDRAWL_XPATH, currency)

    def click_on_confirm_button(self):
        self.click_on_element_by_xpath(CONFIRM_DEPOSIT_OR_WITHDRAWL_BUTTON_XPATH)
