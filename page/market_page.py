from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click((MobileBy.ID,'com.xueqiu.android:id/action_search'))
        return SearchPage(self.driver)