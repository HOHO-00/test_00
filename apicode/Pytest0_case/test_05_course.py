"""
    教程相关接口测试用例
"""

import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file
from utils.filetools import read_file
from utils.exceltools import read_excel

datas = read_excel("data/data.xlsx", "教程")

# 获取教程详情列表
def test_01_course_detail():
    url = datas[0][2]
    header = eval(datas[0][3])
    res = requests.get(url=url,headers=header)
    # print(res.text)
    
    assert res.status_code == datas[0][5]
    assert res.json()["status"] == datas[0][6]