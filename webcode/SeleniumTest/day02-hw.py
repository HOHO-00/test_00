import time
from selenium import webdriver
from seleniumtools import find_element


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://hxtx.testgoup.com/")


# driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys('admin')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/button').click()

# time.sleep(10)
# driver.implicitly_wait(10)  # 实现智能等待，如果元素网页加载出来了，就会继续往下执行，不会一直等
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[1]/span').click()
# # time.sleep(10)
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/input').send_keys('二哈')
# driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]').click()

# time.sleep(10)
# e = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div')
# assert e.text == "二哈"


username = ('xpath', '//*[@id="app"]/div/div/form/div[1]/div/div/input')
password = ('xpath', '//*[@id="app"]/div/div/form/div[2]/div/div/input')
loginbtn = ('xpath', '//*[@id="app"]/div/div/form/div[3]/button')
lbtlinke = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[1]/span')
searchke = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/input')
searchan = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
reseleme = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div')

# 登录
find_element(driver, username).send_keys('admin')
find_element(driver, password).send_keys('123456')
find_element(driver, loginbtn).click()

# 点击轮播图按钮
find_element(driver, lbtlinke).click()

# 输入二哈，并且点击搜索
find_element(driver, searchke).send_keys('二哈')
find_element(driver, searchan).click()

# 断言结果
e = find_element(driver, reseleme)
assert e.text == '二哈'