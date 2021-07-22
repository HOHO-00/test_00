import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://ctw.testgoup.com/html/login.html")
time.sleep(3)

driver.find_element_by_id('username').send_keys('123')
driver.find_element_by_id('password').send_keys('123')
driver.find_element_by_id('userLogin').click()
time.sleep(3)

# 弹窗alerts
driver.switch_to_alert().accept()   # 点击alert的确定按钮
# driver.switch_to_alert().dismiss()  # 点击alert的取消按钮
