"""
    固定的用法，知道怎么用就行了
"""
from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator, timeout=60):
    """
        方法：显式等待，动态查找元素
        参数：
            driver：浏览器的句柄、把柄
            locator:元素定位的方式和值
                - ('id', 'kw')                      # driver.find_element_by_id
                - ('xpath', 'xxxxx')
                - ('name', 'xxx')
                - ('css selector', 'xxxx')
                - ('class name', 'xxxx')            # driver.find_element_by_class_name
                - ('link text', 'xxxx')             # driver.find_element_by_link_text
                - ('partial link text', 'xxx')      # driver.find_element_by_partial_link_text
            timeout：超时时间，默认为60
        返回值：
            找到元素就返回元素本身，没有找到元素就报错
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))