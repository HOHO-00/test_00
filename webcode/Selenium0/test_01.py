# 导入selenium
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()   # 网页最大化
driver.get("http://tomcat-69.gis-data.cn:7080/tdfkweb/#/user-login")

driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[1]/div/div/input').send_keys('admin')  # 输入账号
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[2]/div/div/input').send_keys('123456') # 输入密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[4]/div/button').click()               # 点击登录

time.sleep(3)

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div').click() # 点击待办合计
time.sleep(3)

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[1]/div/div/div/input').send_keys('合川区')  # 输入合川区
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[11]/div/div/button[2]/span').click() # 点击搜索结果第一个项目的地块管理


time.sleep(3)
e = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[7]/div/span')  # 判断地块阶段是否处于土地复垦方案阶段
assert e.text == '土地复垦方案阶段'

# 断言2：元素是否存在
# time.sleep(3)
# e = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[7]/div/span')  # 判断地块阶段是否处于土地复垦方案阶段
# assert len(e) != 0

print("执行成功")

# 退出测试
driver.quit()



