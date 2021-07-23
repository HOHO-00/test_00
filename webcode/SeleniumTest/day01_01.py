# 导入selenium
from selenium import webdriver
from seleniumtools import find_element

# 1、打开浏览器：实例化浏览器句柄/把柄
# Chrome:大写的C,不要小写
# driver：句柄、把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2、打开浏览器网页
driver.get("https://www.baidu.com/")

# 3、元素定位
# id定位(id是唯一的)
# 输入框的标签<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# driver.find_element_by_id('kw').send_keys('selenium')
input = ('id','kw')
find_element(driver,input).send_keys('selenium')

# name定位
# driver.find_element_by_name('wd').send_keys('selenium')

# classname定位
# driver.find_element_by_class_name('s_ipt').send_keys('selenium')

# css selector定位
# driver.find_element_by_css_selector('#kw').send_keys('selenium')

# link text定位
# driver.find_element_by_link_text('学术').click()

# # partial_link_text定位
# driver.find_element_by_partial_link_text('学').click()

# tag name定位
# driver.find_element_by_tag_name()

# xpath定位
# //*[@id="su"]
# driver.find_element_by_xpath('//*[@id="su"]').click()
searchbt = ('xpath','//*[@id="su"]')
find_element(driver,searchbt).click()




