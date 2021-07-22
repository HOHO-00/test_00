"""
    灵感相关接口测试用例
"""

import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "灵感")

# 发表灵感
def test_01_inspire_add():
    url = datas[0][2]
    header = eval(datas[0][3])
    data = eval(datas[0][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

    inspireid = res.json()["data"]["inspirerid"]
    write_file('./tmp/inspire_id.txt',str(inspireid))

    sql = "select * from t_inspirer where id = {}".format(read_file("./tmp/inspire_id.txt"))
    assert len(query(sql)) != 0

# 获取灵感详情
def test_02_inspire_details():
    iid = read_file("./tmp/inspire_id.txt")  
    url = datas[1][2]+"?iid={}".format(iid)
    header = eval(datas[1][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)

    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]

# 修改灵感
def test_03_inspire_update():
    url = datas[2][2]
    header = eval(datas[2][3])
    data = eval(datas[2][4])
    res = requests.post(url=url,headers=header,json=data)  
    # print(res.text)

    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]

    content = eval(datas[2][4])["content"]
    sql = "select * from t_inspirer where id = {} and content = '{}'".format(read_file("./tmp/inspire_id.txt"),content)
    assert len(query(sql)) != 0

# 删除灵感
def test_04_inspire_delete():
    url = datas[3][2]
    header = eval(datas[3][3])
    data = eval(datas[3][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[3][5]
    assert res.json()["status"] == datas[3][6]

    sql = "select * from t_inspirer where id = {} and status = '1'".format(read_file("./tmp/inspire_id.txt"))  # status：0正常；1删除；2禁用
    assert len(query(sql)) != 0
    