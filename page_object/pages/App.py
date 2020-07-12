# * coding:utf-8 *
# Author:sisul
#创建时间：2020/7/12 10:15
from page_object.driver.AndroidClient import AndroidClient
from page_object.pages.MainPage import MainPage


class App:
    @classmethod
    def main(cls):
        AndroidClient.restartApp()
        return MainPage()