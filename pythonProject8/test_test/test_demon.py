#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/27 20:36
# @Author : 小野夏
# @Site : 
# @File : test_demon.py
# @Software: PyCharm
import time


import unittest
from poium import PageElement, Page, PageElements
from selenium import webdriver


class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = PageElement(id_="wd")
    search_button = PageElement(id_='su')


class TestBaidu(unittest.TestCase):
    """百度搜索测试用例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case1(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()

    def test_baidu_search_case2(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "unittest"
        page.search_button.click()

    def test_baidu_search_case3(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "page object"
        page.search_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main':
    unittest.main(verbosity=2)