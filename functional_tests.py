import unittest
from selenium import webdriver
import time
class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_open_shop_home_page(self):
        """Тест: открыть сайт магазина и убедится в правильности"""
        self.browser.get('http://localhost:5000/')
        time.sleep(3)
        self.assertIn("",self.browser.title)
        self.fail('Закончить тест')

if __name__ == "__main__":
    unittest.main(warnings='ignore')