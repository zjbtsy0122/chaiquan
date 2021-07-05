# 练习1：
# 通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
# 练习2：
# 使用代码，实现一个注册的功能。
# 用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
# 储到字典中，{username:password}

# 答案1
# light = {"红灯":30 ,"绿灯":35 ,"黄灯":3}
# while True:
#     for i in light :
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")

# 答案2

username = input("请输入账号：")
password = input("请输入密码：")

if len(username) >=5 and len(username)<=8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password) >=6 and len(password) <= 12:
            print("注册成功！",{username:password})
        else:
            print("密码必须是6-12位") 
    else :
        print("账号的首字母必须小写开头")
else :
    print("账号长度不符合规范，请输入长度是5-8位")

