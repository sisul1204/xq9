#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/13 17:33
# file: ProfilePage.py
from page_object.pages.BasePage import BasePage
from page_object.pages.LoginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        self.findByText('登录雪球').click()
        return LoginPage()