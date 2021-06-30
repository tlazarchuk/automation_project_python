from pages.base_page import BasePage
from pages.home_page import HomePage

ADD_CUSTOMERS_BUTTON_XPATH = '//body/div/div/div[2]/div/div[1]/button[1]'
OPEN_ACCAOUNT_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/button[2]'
CUSTOMERS_BUTTON_XPATH = '//body/div[1]/div/div[2]/div/div[1]/button[3]'
FIRST_NAME_XPATH = '/html/body/div[1]/div/div[2]/div/div[2]/div/div/form/div[1]/input'
LAST_NAME_XPATH = '//body/div[1]/div/div[2]/div/div[2]/div/div/form/div[2]/input'
POST_CODE_XPATH = '//body/div[1]/div/div[2]/div/div[2]/div/div/form/div[3]/input'
CREATE_CUSTOMER_XPATH = '//body/div[1]/div/div[2]/div/div[2]/div/div/form/button'
SEARCH_CUSTOMER_XPATH = '//body/div/div/div[2]/div/div[2]/div/form/div/div/input'
BUTTON_DELETE_WHEN_SEARCH_XPATH = '//body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[5]/button'
PROGRESS_OPEN_ACCOUNT_XPATH = '//body/div/div/div[2]/div/div[2]/div/div/form/button'
USER_SELECT_XPATH = '//*[@id="userSelect"]/option[text()="Alberto Del Rio"]'
CURRENCY_POUND_XPATH = '//*[@id="currency"]/option[text()="Pound"]'
ACCOUNT_NUMBER = ''


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

    def accept_popup(self):
        alert = self.driver.switch_to.alert
        alert.accept()

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

    def fill_search_input_using_name(self, name):
        self.fill_in_text_field_by_xpath(SEARCH_CUSTOMER_XPATH, name)

    def delete_customer_when_search(self):
        self.click_on_element_by_xpath(BUTTON_DELETE_WHEN_SEARCH_XPATH)

    def if_customer_exist(self, name):
        self.fill_search_input_using_name(name)
        try:
            self.click_on_element_by_xpath(BUTTON_DELETE_WHEN_SEARCH_XPATH)
            return True
        except:
            return False

    def clear_search_input(self):
        self.find_element_by_xpath(SEARCH_CUSTOMER_XPATH).clear()

    def create_test_customer(self):
        """Creating customer with test data"""
        self.click_on_add_customer_button()
        self.create_customer_with_filds('Alberto', 'Del Rio', 'E800000')
        self.click_on_create_customer_button()
        self.accept_popup()

    def select_customer_in_list(self):
        self.click_on_element_by_xpath(USER_SELECT_XPATH)
        self.click_on_element_by_xpath(CURRENCY_POUND_XPATH)
        self.click_on_element_by_xpath(PROGRESS_OPEN_ACCOUNT_XPATH)

    def get_response_from_popup_account_number(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        return text[-4:]
