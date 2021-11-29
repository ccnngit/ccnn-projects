from test_case.baidu_page import BaiduPage
import unittest
from selenium import webdriver
from time import sleep

class TestBaidu(unittest.TestCase):
    """百度搜索测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.open('https://www.baidu.com')
        page.search_input.send_keys('selenium')
        page.search_button.click()
        sleep(3)
        self.assertEqual(page.get_title, 'selenium_百度搜索')




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()    #  verbosity=3