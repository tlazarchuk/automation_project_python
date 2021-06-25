from selenium.common.exceptions import TimeoutException

from pages import base_page
from pages.base_page import BasePage

ADD_CUSTOMERS_BUTTON_XPATH = '//body/div/div/div[2]/div/div[1]/button[1]'
OPEN_ACCAOUNT_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/button[2]'
CUSTOMERS_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/button[3]'
FIRST_NAME_XPATH = '/html/body/div[1]/div/div[2]/div/div[2]/div/div/form/div[1]/input'
LAST_NAME_XPATH = '//body/div[1]/div/div[2]/div/div[2]/div/div/form/div[2]/input'
POST_CODE_XPATH = '//body/div[1]/div/div[2]/div/div[2]/div/div/form/div[3]/input'
CREATE_CUSTOMER_XPATH = '//body/div[1]/div/div[2]/div/div[2]/div/div/form/button'

"""Class for the Manager page with methods which using for testing"""

class ManagerPage(BasePage):

    def click_on_add_customer_button(self):
        self.click_on_element_by_xpath(ADD_CUSTOMERS_BUTTON_XPATH)

    def click_on_open_accaunt_button(self):
        self.click_on_element_by_xpath(OPEN_ACCAOUNT_BUTTON_XPATH)

    def click_on_customers_button(self):
        self.click_on_element_by_xpath(CUSTOMERS_BUTTON_XPATH)

    def fill_first_name_for_test(self, first_name):
        self.fill_in_text_field_by_xpath(FIRST_NAME_XPATH, first_name)

    def fill_last_name_for_test(self, last_name):
        self.fill_in_text_field_by_xpath(LAST_NAME_XPATH, last_name)

    def fill_post_code_for_test(self, post_code):
        self.fill_in_text_field_by_xpath(POST_CODE_XPATH, post_code)

    def click_on_create_customer_button(self):
        self.click_on_element_by_xpath(CREATE_CUSTOMER_XPATH)

    def create_customer_with_filds(self, first_name, last_name, post_code):
        self.fill_first_name_for_test(first_name)
        self.fill_last_name_for_test(last_name)
        self.fill_post_code_for_test(post_code)

    def get_response_from_popup(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        return text[0:27]

    def if_user_created(self):
        try:
            text =  self.get_response_from_popup()
            if(self.correctness_response_from_popup(text)):
                return True
            else:
                return False
        except:
            return False

    def correctness_response_from_popup(self, text):
        if(text == 'Customer added successfully'):
            return True
        else:
            return False