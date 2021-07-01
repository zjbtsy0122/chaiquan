# 判断
# a = 1
# b = 2

# if a > b:
#     print("a比b大")

# else:
#     print("b更大")


a = input("请输入：")
if a in "0123456789":
    a = int(a)
else:
    print("请输入正确的年龄！")
    exit()
if a > 5:
    print("大")
else :
    print("小")
