#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/13 18:52
# file: test_login.py
import pytest

from page_object.pages.App import App


class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().gotoProfile()

    def setup_method(self):
        self.loginPage = self.profilePage.gotoLogin()

    @pytest.mark.parametrize("user, pw, msg",[
        ('182505693010','a1234567','手机号码'),
        ('18250569301','a1234567','密码错误')
    ])
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        assert msg in self.loginPage.getErrorMsg()


    def teardown_method(self):
        self.loginPage.back()


