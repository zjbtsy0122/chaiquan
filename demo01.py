# a = input("请输入：")
# b = input("请输入：")

# print(len(a+b))

#hahaa

#元祖，下标，从0开始编号


a = (1,2,3,4,"哈哈","嘻嘻",True,False)

# print(a[4])
# print(a.index("哈哈"))

#二维元祖
b = (a,"哈哈","嘻嘻")
print(b[0][3])

#切片

print(a[0:4])

# 元祖一定写好过后不可以修改，而数组是可以修改的

c = [1,2,3,4,"哈哈","嘻嘻",True,False]

c.append("奥特曼")
print(c)

c.insert(0,"赛罗")
print(c)

#剪切
c.pop(5)
print(c)

#clear()清空
#extend()

"""
所有的方法都是小括号结尾，print(),input(),len()
元祖、数组、字典的取值，都是用中括号，比如 a[0]
元祖、数组、字典的定义，分别是()、[]、{}
"""
d = {"name":"张三",0:"哈哈","age":25}

#新增
d["high"] = "183cm"
print(d)
#修改
d["name"] = "李四"
print(d)
#get()取value值

#update 修改
d.update(name="王五")
print(d)


'''
练习
获取用户输入的个人信息，并且存储在字典中
个人信息包括了，name，age,sex
'''


aa = input("请输入姓名:")
bb = input("请输入年龄:")
cc = input("请输入性别:")

p = {"name":"haha","age":25,"sex":""}

p.update(name=aa)
p.update(age=bb)
p.update(sex=cc)
print(p)


