# 导入unittest
# 导入unittest
import time
import unittest
from selenium import webdriver

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

    # 成员方法：在每个test_方法结束运行的时候执行一次
    def tearDown(self):
        print("结束")

    # 每个方法就是一个测试用例
    def test_01_search(self):
        self.driver.find_element_by_id('search-input').send_keys('包包')
        self.driver.find_element_by_id('ai-topsearch').click()

        time.sleep(10)
        e = self.driver.find_element_by_xpath('/html/body/div[4]/div/ul/li/div/p[2]/strong')
        # print(e.text)  #输入内容会直接显示在测试报告里面，不显示在终端里面
        assert e.text == '￥168.00'

    # 检查商品价格
    def test_02_check_price(self):
        e = self.driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/div/p')
        assert e.text == '￥356.00'

# 运行：看效果（调试）
if __name__ == "__main__":
    unittest.main()    

# unittest会自动管理selenium在运行完后自动关闭浏览器 
# setUpClass （打开浏览器) > setUp(01) > test_01_search >tearDown(01)   > setUp(02) > test_02 >tearDown(02) ... >  tearDownClass   
# setUp :前置条件；   tearDown：后置条件