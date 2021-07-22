"""
    文章相关接口测试用例
"""

import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "文章")

# 获取文章详情
def test_01_arictle_details():
    url = datas[0][2]
    header = eval(datas[0][3])
    res = requests.get(url=url,headers=header)

    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

# 获取文章评论列表
def test_02_arictle_comments():
    url = datas[1][2]
    header = eval(datas[1][3])
    data = eval(datas[1][4])
    res = requests.post(url=url,headers=header,json=data)

    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]

# 新增文章
def test_03_article_add():
    url = datas[2][2]
    header = eval(datas[2][3])
    data = eval(datas[2][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]

    articleid = res.json()["data"]["articleid"]
    write_file('./tmp/article_id.txt',str(articleid))
    sql = "select * from t_article where id = {}".format(read_file("./tmp/article_id.txt"))
    assert len(query(sql)) != 0


# 修改文章
def test_04_article_update():
    url = datas[3][2]
    """
    payload={}
    files=[('upload',('ho.png',open('C:/users/jssy/Pictures/ho.png','rb'),'image/png'))]
    """
    header = eval(datas[3][3])
    data = eval(datas[3][4])
    res = requests.post(url=url,headers=header,json=data)  # res = requests.post(url=url, json=data, headers=header,data=payload)
    # print(res.text)

    assert res.status_code == datas[3][5]
    assert res.json()["status"] == datas[3][6]

    title = eval(datas[3][4])["title"]
    # sql = "select * from t_article where id = {} and title = '{}'"
    # sql = "select * from t_article where id = {} and title = '为什么要学习测试123'".format(read_file("./tmp/article_id.txt"))
    sql = "select * from t_article where id = {} and title = '{}'".format(read_file("./tmp/article_id.txt"),title)
    # r = query(sql)   
    # assert len(r) != 0
    assert len(query(sql)) != 0

# 删除文章
def test_05_article_delete():
    url = datas[4][2]
    header = eval(datas[4][3])
    data = eval(datas[4][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]

    sql = "select * from t_article where id = {} and status = '1'".format(read_file("./tmp/article_id.txt"))  # status：0正常；1删除；2禁用
    assert len(query(sql)) != 0