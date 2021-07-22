"""
    固定的用法，知道怎么用就行了
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator, timeout=60):
    """
        方法名：显式等待，动态查找元素
        参数：
            driver：浏览器的句柄/把柄
            locator: 元素定的方式和值
                - ("id", "username")
                - ("xpath", "xxxxxxx")
                - ("aid", "xxxxxx")
                - ("text", "xxx")

            timeout：超时时间，默认是60
        注意：
            主需要知道怎么用它

    """
    if locator[0] == 'aid':
        locator = (MobileBy.ACCESSIBILITY_ID, locator[1])
    if locator[0] == "text":
        locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))
