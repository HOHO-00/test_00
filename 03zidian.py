a = {"name":"零零零","password":"000"} #键值对 键（key） 值（value）

#字典取值:
print(a["name"]) #通过key值来取
print(a.get("name"))#通过get的方式来取值

print(a["hh"]) #如果键不存在，这种方式报错
print(a.get("hh")) #这种方式不报错

#修改
a["name"] = "零零"
print(a)

#第二种方法 修改 （复杂）
a.update({"name":"嘻嘻零"})
print(a)

#添加
#第一种方法
a.update({"sex":"女"})
print(a)

#第二种方法
a["age"] = 18
print(a)

#删除
a.pop("sex")
print(a)

