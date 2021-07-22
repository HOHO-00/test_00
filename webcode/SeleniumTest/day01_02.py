# 导入selenium
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()   # 网页最大化
driver.get("http://hxtx.testgoup.com/#/login")

driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys('123456')
driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/button').click()

time.sleep(5)

# 断言1：通过文本值
# e = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[1]/span')
# assert e.text == '轮播图管理'

# 断言2：元素是否存在
# find_elements_by_xxx:找到元素 list就有长度；没有找到元素 list长度为0
e = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/ul/li[1]/span')
assert len(e) != 0

print("执行成功")
print(driver.current_url)   # 获取网页的地址
print(driver.title)         # 获取网页的标题

# 退出测试：自动关闭浏览器，销毁driver
driver.quit()