from pages.base_page import BasePage

BACK_BUTTON_XPATH = '//body/div/div/div[2]/div/div[1]/button[1]'
FIRST_IN_LIST_TRANSACTION_TYPE_XPATH_XPATH = '//body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]'
SECOND_IN_LIST_TRANSACTION_TYPE_XPATH = '//body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]'
RESET_BUTTON_XPATH = '//body/div/div/div[2]/div/div[1]/button[2]'

"""Class for the Transaction page with methods which using for testing"""

class TransactionPage(BasePage):

    def click_on_back_button(self):
        self.click_on_element_by_xpath(BACK_BUTTON_XPATH)

    def get_first_in_list_transaction_type(self):
        try:
            return self.find_element_by_xpath(FIRST_IN_LIST_TRANSACTION_TYPE_XPATH_XPATH).text
        except:
            return False 

    def get_second_in_list_transaction_type(self):
        try:
            return self.find_element_by_xpath(SECOND_IN_LIST_TRANSACTION_TYPE_XPATH).text
        except:
            return False

    def click_on_reset_button(self):
        self.click_on_element_by_xpath(RESET_BUTTON_XPATH)

    def find_first_in_list_transaction_type(self):
        try:
            self.find_element_by_xpath(FIRST_IN_LIST_TRANSACTION_TYPE_XPATH_XPATH)
            return True
        except:
            return False
 