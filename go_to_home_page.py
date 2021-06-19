import unittest
import time

from selenium import webdriver

from pages import home_page as hp

class GotoHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = hp.HomePage(self.driver)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_go_to_home_page(self):
        # self.login_page.sign_in_as_client()
        # self.cart_page.click_on_restaurants_list()
        # self.cart_page.click_on_watch_menu()
        # self.cart_page.make_order_first_dish()
        # dish = self.cart_page.get_name_from_first_dish()
        # dish_in_cart = self.cart_page.get_name_of_dish_in_cart()
        print("Hello world!")
        self.home_page.go_to_home_page()
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

if __name__ == "__main__":
  unittest.main()
