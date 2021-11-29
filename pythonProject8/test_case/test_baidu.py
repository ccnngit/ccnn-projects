#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 14:28
# @Author : 小野夏
# @Site : 
# @File : test_baidu.py
# @Software: PyCharm
import unittest
from time import sleep
from selenium import webdriver
from test_case.baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input('selenium')
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(), "selenium_百度搜索")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()