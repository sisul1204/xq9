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
    def test_price(self):
        assert cls.main.gotoSelected().getPriceByName('比亚迪') == 89

    def test_is_selected_stock(self):
        searchPage = App.main().gotoSearch().search('alibaba')
        assert searchPage.isInSelected('BABA') == True
        assert searchPage.isInSelected('09988') == False

    def test_is_follow_user(self):
        pass
