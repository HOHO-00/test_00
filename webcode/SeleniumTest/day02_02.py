import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://192.168.1.233:9000/shopxo")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/a/img').click()  # 点击商品
time.sleep(1)
# 获取所有窗口的句柄 / 把柄
print(driver.window_handles)
# ['CDwindow-9F0E0A30E08741804DD834C136091AE2', 'CDwindow-BD267B8A8A287CC2A33EB848BEE7B81B']

# 切换到最新的window
driver.switch_to_window(driver.window_handles[-1])

driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button').click() # 点击立即购买
