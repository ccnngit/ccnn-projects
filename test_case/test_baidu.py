from test_case.baidu_page import BaiduPage




class TestBaidu(unittest.TestCase):
    """百度搜索测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.get_url("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()
        self.assert(page.get_title(), 'selenium_百度搜索')



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main':
    unittest.main(verbosity=2)