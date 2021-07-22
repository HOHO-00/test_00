# 导入unittest
import time
import unittest
from selenium import webdriver

# 类
class TestCaseIndex(unittest.TestCase):

    def test_01_login_success(self):
        print("登录代码")

    def test_02_login_failed(self):
        print('这是登录失败的测试用例')