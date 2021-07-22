"""
    问题相关接口测试用例
"""

import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file
from utils.filetools import read_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "问题")

# 新增问题
def test_01_new_question():
    url = datas[0][2]
    header = eval(datas[0][3])
    data = eval(datas[0][4])
    res = requests.post(url=url , headers=header, json=data)
    # print(res.text)

    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]

    # 数据库校验
    questionid = res.json()["data"]["questionid"]
    write_file('./tmp/question_id.txt',str(questionid))
    sql = "select * from t_questions where id = {}".format(read_file("./tmp/question_id.txt"))
    assert len(query(sql)) != 0

# 获取问题详情
def test_02_question_detail():
    url = datas[1][2]
    header = eval(datas[1][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)
       
    assert res.status_code == datas[1][5]
    assert res.json()["status"] == datas[1][6]