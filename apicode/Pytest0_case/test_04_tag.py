"""
    标签相关接口测试用例
"""

import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file
from utils.filetools import read_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "标签")

# 获取教程标签列表
def test_01_tag_course():
    url = datas[0][2]
    header = eval(datas[0][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)
    
    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

# 获取问题标签列表
def test_01_tag_question():
    url = datas[1][2]
    header = eval(datas[1][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)
    
    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]

# 获取文章标签列表
def test_01_tag_article():
    url = datas[2][2]
    header = eval(datas[2][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)
    
    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]