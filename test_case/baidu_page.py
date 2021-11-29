from poium import Page, Element


class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = Element(id_="kw")
    search_button = Element(id_='su')


