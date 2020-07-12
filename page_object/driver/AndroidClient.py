# * coding:utf-8 *
# Author:sisul
#创建时间：2020/7/12 7:41
from appium.webdriver import webdriver
from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class AndroidClient:
    driver:WebDriver
    @classmethod
    def installApp(cls) -> WebDriver:
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'oneplus'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        #解决第一次启动的问题
        caps['autoGrantPermissions'] ='true'

        cls.driver = webdriver.Remote('http://localhost:4273/wd/hub', caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restartApp(cls):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'oneplus'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        caps['noReset'] = True

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
