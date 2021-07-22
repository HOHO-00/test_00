import time
from selenium import webdriver
from seleniumtools import find_element


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.bilibili.com/")

# time.sleep(20)
# print(driver.get_cookies())

driver.delete_all_cookies()
cookies = [{'domain': '.bilibili.com', 'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': 'caab6daf19bd3ff81f7beac9b007b57b'},
 {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '319530624'}, 
 {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'buvid_fp_plain', 'path': '/', 'secure': False, 'value': '303BB0A2-6F98-43C9-8EFE-5CB10B5789DA18552infoc'},
  {'domain': '.bilibili.com','httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': '23899e5c%2C1627222067%2Cf43db*11'},
   {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'buvid_fp', 'path': '/', 'secure': False, 'value': '303BB0A2-6F98-43C9-8EFE-5CB10B5789DA18552infoc'}, 
   {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': '9oqdtr0s'}, {'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 'secure': False, 'value': '1777945899'}, 
   {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': '303BB0A2-6F98-43C9-8EFE-5CB10B5789DA18552infoc'}, 
   {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '8625de1275fc4bf8'}, 
   {'domain': '.bilibili.com', 'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': 'F2039572-5771-08DC-FAE4-57A10359A8D452538infoc'},
    {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'fingerprint', 'path': '/', 'secure': False, 'value': '4015b4d3552380a359f157dd47dae81d'}]

for c in cookies:
    driver.add_cookie(c)

driver.refresh()