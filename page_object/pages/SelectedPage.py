# * coding:utf-8 *
# Author:sisul
#创建时间：2020/7/12 7:18
from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.pages.BasePage import BasePage


class SelectedPage(BasePage):


    def addDefault(self):
        return self

    def getPriceByName(self, name):
        # price = self.driver\
        #     .find_element_by_xpath("//*[contains(@resource-id, 'stockName') and @text='"+name+"']/../../..//*[contains(@resource-id,'currentPrice')]").text


        priceLocator = (By.XPATH, "//*[contains(@resource-id, 'stockName') and @text='%s']/../../..//*[contains(@resource-id,'currentPrice')]" %name)
        price = self.find(priceLocator).text
        return float(price)