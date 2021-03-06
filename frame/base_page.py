from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from frame import handle_black


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver
    @handle_black
    def find(self,locator):
            return self.driver.find_element(*locator)


    def find_and_click(self,locator):
        self.find(locator).click()

    def find_and_text(self,locator,text):
        self.find(locator).send_keys(text)

    def scroll_find_click(self,text):
        element=(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')

        self.find_and_click(element)

    def find_and_get_text(self,locator):
        return self.find(locator).text