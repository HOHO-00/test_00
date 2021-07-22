"""
    首页相关接口测试用例
"""

import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file
from utils.filetools import read_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx","首页")

# 获取首页轮播图
def test_01_titleimg():
    # 构造请求
    url = datas[0][2]
    header = eval(datas[0][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    # 断言
    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

    # 数据库校验

# 获取推荐教程
def test_02_course():
    url = datas[1][2]
    header = eval(datas[1][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]

# 获取热门讨论
def test_03_question():
    url = datas[2][2]
    header = eval(datas[2][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]

# 获取热门文章
def test_04_article():
    url = datas[3][2]
    header = eval(datas[3][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[3][5]
    assert res.json()["status"] == datas[3][6]

# 获取灵感
def test_05_inspire():
    url = datas[4][2]
    header = eval(datas[4][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[4][5]
    assert res.json()["status"] == datas[4][6]

# 获取活跃用户
def test_06_activeuser():
    url = datas[5][2]
    header = eval(datas[5][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[5][5]
    assert res.json()["status"] == datas[5][6]