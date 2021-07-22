import time
import unittest
from selenium import webdriver
from utils import cookie

# 类
class TestCaseIndex(unittest.TestCase):

    # 类方法：在类开始运行的时候执行一次：初始化
    # cls = self
    # cls：表示类的本身;   self：实例化对象本身
    # cls只在类方法里用
    # 固定的 直接写
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()

    # 类方法：在类结束的时候做释放资源操作
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()   # 让每个py文件运行完后就可以关闭浏览器（每运行完一个py文件就可以先关掉这个浏览器窗口），而不需要等到所有py文件运行完由unittest来管理selenium关闭浏览器

    # 成员方法：在每个test_方法运行的时候执行一次
    def setUp(self):
        print("开始")
        self.driver.get('http://118.24.255.132:19999/shopxo/')
        # 绕过登录，提前登录
        # step1：手动登录并且获取已经登录的cookie
        # time.sleep(20)
        # print(self.driver.get_cookies())

        # step2：删除原有的cookie，使用已经登录的cookie来绕过登录限制
        self.driver.delete_all_cookies()
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def test_01_buy_goods(self):
        self.driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/a/img').click()
        time.sleep(10)

        # 切换到新窗口
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('').click()
        
        # 最后一定要去购物车去判断结果