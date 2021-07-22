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

e = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div[1]/div')
ActionChains(driver).move_to_element(e).perform()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/ul/li[3]/span').click()  # 点击退出登录
time.sleep(1)

e1 = driver.find_element_by_xpath('/html/body/div[2]/div/div')  # 弹出提示“退出登录成功~”
# e2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[4]/div/button') #跳转至登录页面-登录按钮
assert e1.text == '退出登录成功~'
# assert e2.text == '登录'
time.sleep(2)

e2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[4]/div/button') #跳转至登录页面-登录按钮
assert e2.text == '登录'

print('执行成功')

driver.quit()
