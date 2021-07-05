
def checkname(username):
    if len(username) >=5 and len(username)<=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            
            print("ok") 
        else :
            print("账号的首字母必须小写开头")
    else :
        print("账号长度不符合规范，请输入长度是5-8位")


#包>类>方法>变量