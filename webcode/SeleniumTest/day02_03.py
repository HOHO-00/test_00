import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://192.168.1.233:9000/shopxo/admin.php")
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys('shopxo')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
time.sleep(5)

# 把作用域切换到子页面
iframe = driver.find_element_by_id('ifcontent')
driver.switch_to_frame(iframe)

a = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]').text
print(a)

# 作用域切换到父页面
driver.switch_to_default_content()