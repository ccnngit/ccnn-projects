#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 21:15
# @Author : 小野夏
# @Site : 
# @File : test_baidu_poium.py
# @Software: PyCharm
from test_case.baidu_page_poium import BaiduPage
import unittest
from selenium import webdriver
from time import sleep


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_baidu_poium(self):
        page = BaiduPage(self.driver)
        # page.get_url('https://www.baidu.com')
        # page.get_url('https://www.baidu.com')
        page.open('https://www.baidu.com')
        page.search_input.send_keys('selenium')
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title, 'selenium_百度搜索')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
