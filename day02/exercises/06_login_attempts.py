key = 123456
for i in range(3):
    keyin = int(input('请输入密码:'))
    if keyin ==key:
        print('登录成功')
        break
    else:
        print("密码不正确请重新输入")
else:
    print("账号已锁定")