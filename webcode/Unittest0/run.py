"""
    整个项目的运行入口
"""

import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 1、自动查找所有的测试用例
testcase = unittest.defaultTestLoader.discover('case','test_*.py')

# 2、使用htmltestrunner工具来帮助我们自动运行所有的case和生成测试报告
title = "web自动化测试报告"
descr = "这是第一次实现web自动化测试"
filepath = "./report/report.html"

with open(filepath,"wb") as f:   # wb：字节方式写入
    runner = HTMLTestRunner(stream=f,title=title,description=descr)
    runner.run(testcase)