import unittest
import time

from selenium import webdriver

from pages import home_page as hp

class GotoHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = hp.HomePage(self.driver)
        self.home_page.go_to_home_page()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_go_to_home_page(self):
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def test_check_home_button(self):
        self.home_page.click_on_home_button()
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

if __name__ == "__main__":
  unittest.main()
