# * coding:utf-8 *
# Author:sisul
#创建时间：2020/7/12 7:28

import pytest

from page_object.pages.App import App
from page_object.pages.MainPage import MainPage


class TestSelected:
    mainPage:MainPage
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.mainPage = TestSelected.mainPage
        self.searchPage = self.mainPage.gotoSearch()

    def test_price(self):
        assert self.searchPage.getPriceByName('比亚迪') == 89

    def test_is_selected_stock(self):
        self.searchPage.search('alibaba')
        assert self.searchPage.isInSelected('BABA') == True
        assert self.searchPage.isInSelected('09988') == False

    @pytest.mark.parametrize("key, code", [
        ('招商银行', 'SH600036'),
        ('平安银行', 'SZ000001'),
        ('pingan', 'SH601318')
    ])
    def test_is_selected_stock_hs(self, key, code):
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code) == False

    def teardown_method(self):
        self.searchPage.cancel()



    def test_is_add_stock_hs(self):
        key = '招商银行'
        code = 'SH600036'
        self.searchPage.search(key)
        if self.searchPage.isInSelected(code) == True:
            self.searchPage.removeFromSelected(code)
        self.searchPage.addToSelected(code)

        assert self.searchPage.isInSelected(code) == True


    def test_is_follow_user(self):
        pass
