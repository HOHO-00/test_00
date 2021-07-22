import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

# 上传图片接口
def test_01_upload():
    token = read_file("./tmp/user_token.txt")
    url = "http://118.24.255.132:2333/upload"
    payload={}
    # files=[('file',('ho.png',open('/D:/ho.png','rb'),'image/png'))]
    files=[('file',('picture_test.jpg',open('./data/picture_test.jpg','rb'),'image/jpeg'))]
    # headers = {'Content-Type': 'multipart/form-data','token': token}
    headers = {}

    # response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response = requests.post(url=url,headers=headers,data=payload,files=files)
    print(response.text)
    # 返回值里返回的图片地址如Db4Mo5FjfN0gcjL.jpg可用于文章等接口上传的图片参数

    img = response.json()["data"]
    write_file("./tmp/img.txt",img)