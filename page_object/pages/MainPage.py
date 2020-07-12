# * coding:utf-8 *
# Author:sisul
#创建时间：2020/7/12 7:14
from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.pages.BasePage import BasePage
from page_object.pages.SearchPage import SearchPage
from page_object.pages.SelectedPage import SelectedPage


class MainPage(BasePage):

    def gotoSelected(self):

        # self.driver.find_element(By.XPATH, '//*[@text="自选"]')

        zixuan = '自选'
        self.findByText(zixuan)

        # self.driver.find_element_by_xpath('//*[@text="自选"]')
        self.findByText(zixuan).click()
        return SelectedPage()


    def gotoSearch(self):
        search_button = (By.ID, 'home_search')
        self.find(search_button).click()
        return SearchPage()