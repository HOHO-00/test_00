import time
from selenium import webdriver
from seleniumtools import find_element


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://118.24.255.132:19999/shopxo/")
# 手动登录
# time.sleep(30)
# print(driver.get_cookies())

# 2. 使用登录之后的cookie去访问网页，就能绕过登录
driver.delete_all_cookies() # 删除原有的cookie
cookie = {'domain': '118.24.255.132', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '4tpkohfpmndjtn4325fjjd5614'}  # driver.get_cookies()获取到的cookie
driver.add_cookie(cookie)   # 添加已经登录的cookie
driver.refresh()            # 刷新页面，会自动发送手动添加的