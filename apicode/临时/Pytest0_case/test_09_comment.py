"""
    评论相关接口测试用例
"""

import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "评论")

# 发表一个灵感用来进行评论测试
def test_01_comment_inspire():
    url = datas[0][2]
    header = eval(datas[0][3])
    data = eval(datas[0][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

    inspireid = res.json()["data"]["inspirerid"]
    write_file('./tmp/comment_inspire_id.txt',str(inspireid))

# 发表评论
def test_02_comment_add():
    url = datas[1][2]
    header = eval(datas[1][3])
    data = eval(datas[1][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)   
    # 发表评论成功返回值里没有cid（评论id）

    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]

    commenttype = eval(datas[1][4])["ctype"]
    comment = eval(datas[1][4])["comment"]
    sql = "select * from t_user_comments where ctype = '{}' and fid = {} and uid = {} and comment = '{}'".format(commenttype,read_file("./tmp/comment_inspire_id.txt"),read_file("./tmp/user_id.txt"),comment)
    # print(query(sql))
    commentid = (query(sql))[0][0]
    write_file('./tmp/comment_id.txt',str(commentid))
    assert len(query(sql)) != 0

# 获取评论列表
def test_03_getcomment():
    url = datas[2][2]
    header = eval(datas[2][3])
    data = eval(datas[2][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[2][5]
    assert res.json()["status"] == datas[2][6]

# 修改评论
def test_04_comment_update():
    url = datas[3][2]
    header = eval(datas[3][3])
    data = eval(datas[3][4])
    res = requests.post(url=url,headers=header,json=data)  
    # print(res.text)

    assert res.status_code == datas[3][5]
    assert res.json()["status"] == datas[3][6]

    comment = eval(datas[3][4])["comment"]
    sql = "select * from t_user_comments where id = {} and comment = '{}'".format(read_file("./tmp/comment_id.txt"),comment)
    assert len(query(sql)) != 0

# 删除评论
def test_05_comment_delete():
    url = datas[4][2]
    header = eval(datas[4][3])
    data = eval(datas[4][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)

    assert res.status_code == datas[4][5]
    assert res.json()["status"] == datas[4][6]

    sql = "select * from t_user_comments where id = {} and status = '1'".format(read_file("./tmp/comment_id.txt"))  # status：0正常；1删除；2禁用
    assert len(query(sql)) != 0

