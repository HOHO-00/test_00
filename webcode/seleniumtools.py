"""
    固定的用法，知道怎么用就行了
"""

from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator, timeout=60):
    """
        方法名：显式等待，动态查找元素
        参数：
            driver：浏览器的句柄/把柄
            locator: 元素定的方式和值
                - ("id", "username")
                - ("xpath", "xxxxxxx")
                - ("name", "xxxxxx")
                - ("css selector", "xxxxx")
                - ("class name", "xxxxxxxx")
                - ("link text", "抗击肺炎")
                - ("partial link text", "抗击肺")
            timeout：超时时间，默认是60
        注意：
            主需要知道怎么用它

    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))
