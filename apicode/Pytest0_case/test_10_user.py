"""
    用户相关接口测试用例
"""

import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "用户")

# 获取用户详情
def test_01_user():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[0][2]+"?uid={}".format(uid)
    header = eval(datas[0][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

# 获取用户灵感列表
def test_02_user_inspire():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[1][2]+"?uid={}&pagenum=1".format(uid)
    header = eval(datas[1][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]

# 获取用户文章列表
def test_03_user_article():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[2][2]+"?uid={}&pagenum=1".format(uid)
    header = eval(datas[2][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]

# 获取用户问题列表
def test_04_user_question():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[3][2]+"?uid={}&pagenum=1".format(uid)
    header = eval(datas[3][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[3][5]
    assert res.json()["status"] == datas[3][6]

# 获取用户关注人列表
def test_05_user_follow():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[4][2]+"?uid={}".format(uid)
    header = eval(datas[4][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[4][5]
    assert res.json()["status"] == datas[4][6]

# 获取用户粉丝列表
def test_06_user_fan():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[5][2]+"?uid={}".format(uid)
    header = eval(datas[5][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[5][5]
    assert res.json()["status"] == datas[5][6]

# 获取用户动态列表
def test_07_user_dynamic():
    uid = read_file("./tmp/user_id.txt")  
    url = datas[6][2]+"?uid={}&pagenum=1".format(uid)
    header = eval(datas[6][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[6][5]
    assert res.json()["status"] == datas[6][6]