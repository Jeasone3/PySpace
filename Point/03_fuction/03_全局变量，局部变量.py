a = 100
b = 200

def test():
    c = '你好'
    d = 'hehe'
    #a = 300 局部变量和全局变量重名时执行局部变量:就近原则
    global a  # global:可以在局部作用声明全局变量，修改全局变量
    a = 300
    print('函数中的打印(a)',a)
    print('函数中的打印(b)',b)
    print('函数中的打印(c)',c)
    print('函数中的打印(d)',d)

test()
print('全局变量(a)',a)
print('全局变量(b)',b)
print(id(a))