from pages.base_page import BasePage

LOGIN_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/form/button'
LIST_OF_CUSTOMER_XPATH = '//body/div[1]/div/div[2]/div/form/div/select'
GERMIONA_IN_LIST_XPATH = '//*[@id="userSelect"]/option[2]'
TEST_CUSTOMER_IN_LIST_XPATH = '//*[@id="userSelect"]/option[text()="Alberto Del Rio"]'

"""Class for the Customer page with methods which using for testing"""

class CustomerPage(BasePage):

    def pick_germiona_account(self):
        self.click_on_element_by_xpath(GERMIONA_IN_LIST_XPATH)

    def exist_login_button(self):
        try:
            self.find_element_by_xpath(LOGIN_BUTTON_XPATH)
            return True
        except:
            return False

    def exist_list_of_customers(self):
        try:
            self.find_element_by_xpath(LIST_OF_CUSTOMER_XPATH)
            return True
        except:
            return False

    def pick_test_account(self):
        self.click_on_element_by_xpath(TEST_CUSTOMER_IN_LIST_XPATH)

    def click_on_login_button(self):
        self.click_on_element_by_xpath(LOGIN_BUTTON_XPATH)
