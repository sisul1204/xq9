# * coding:utf-8 *
# Author:sisul
#创建时间：2020/7/12 10:21
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient


class BasePage:
    def __init__(self):
        self.driver = AndroidClient.driver


    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))
