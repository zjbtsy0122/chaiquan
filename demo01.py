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

