"""
    登录接口测试用例
"""

import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file
from utils.filetools import read_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "登录")

# 登录成功
def test_01_login_success():
    url = datas[0][2]
    header = eval(datas[0][3])
    data = eval(datas[0][4])
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)
    
    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

    token = res.json()["data"]["token"]
    write_file("./tmp/user_token.txt",token)

    userid = res.json()["data"]["userinfo"]["uid"]
    write_file("./tmp/user_id.txt",str(userid))

# 登录失败
def test_02_login_fail():
    url = datas[1][2]
    header = eval(datas[1][3])
    data = eval(datas[1][4]) 
    res = requests.post(url=url,headers=header,json=data)
    # print(res.text)
    
    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]