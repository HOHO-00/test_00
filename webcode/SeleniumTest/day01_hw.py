# 导入selenium
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()   # 网页最大化
driver.get("http://hxtx.testgoup.com/#/login")

driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys('admin')  # 输入账号
driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys('123456') # 输入密码
driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/button').click()               # 点击登录

time.sleep(3)
# driver.implicitly_wait(5)  # 隐式等待：实现智能等待，如果网页提前加载出来了就不会等到5秒结束

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[1]').click() # 点击轮播图管理
time.sleep(3)

driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/input').send_keys('二哈')  # 输入二哈
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]').click() # 点击搜索


# time.sleep(3)
# e = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div')
# assert e.text == '二哈'

# 断言2：元素是否存在
time.sleep(3)
e = driver.find_elements_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div')
assert len(e) != 0

print("执行成功")

# 退出测试
driver.quit()