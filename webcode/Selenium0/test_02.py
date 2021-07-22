import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()   # 网页最大化
driver.get("http://tomcat-69.gis-data.cn:7080/tdfkweb/#/user-login")

driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[1]/div/div/input').send_keys('admin')  # 输入账号
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[2]/div/div/input').send_keys('123456') # 输入密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[4]/div/button').click()               # 点击登录

time.sleep(3)

# ActionChains(driver).move_to_element(move).perform()
# e = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div[1]/div') 
# ActionChains(self.driver).move_to_element(e).perform()

e = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div[1]/div')
ActionChains(driver).move_to_element(e).perform()
time.sleep(2)

# driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/ul/li[1]').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/ul/li[1]/span').click()
time.sleep(2)

e1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div')  # 个人中心-页面中心标题“基本信息”
e2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/form/div[1]/div/div/input')  # 登录账号框
value = e2.get_attribute('value')
# print(v)
assert e1.text == '基本信息'
assert value == 'admin'

print("执行成功")

driver.quit()