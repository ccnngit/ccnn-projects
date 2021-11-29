#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 21:12
# @Author : 小野夏
# @Site : 
# @File : baidu_page_poium.py
# @Software: PyCharm
# from poium import Page, PageElement
#
#
# class BaiduPage(Page):
#     """
#     百度Page层，百度页面封装操作到的元素
#     """
#     search_input = PageElement(id_ = 'kw')
#     search_button = PageElement(id_ = 'su')
from poium import Page, Element


class BaiduPage(Page):
    """
    百度Page层，百度页面封装操作的元素
    """
    search_input = Element(id_="kw")
    search_button = Element(id_="su")


