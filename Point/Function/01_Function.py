"""Function"""

# py中function先定义再使用
#
# def welcome():
#     print('你好')
#     print('hehe')
#     pass
#
# welcome()

# def order(num,dish):
#     print(f'您点的是{num}份{dish}')
#     pass
#
# order(1,'辣椒炒肉')

# def greet(name,gender,age,height):
#     print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')
#     pass
# # 关键字参数
# greet(name='张三',gender='男',age=18,height=172)
# # 位置参数
# greet('李四','女',18,189)
# # 位置参数要放在关键字参数的前面
# greet('张三','男',age=18,height=177)

# 限制传参方式
# / 前面只能是位置参数，*后面只能是关键字参数
# /必须再*之前
#
# # 正确示例
# greet('张三','男',age=18,height=177)
# greet('张三',gender='男',age=18,height=178)
# # 错误示例
# greet(name='张三',gender='男',age=19,height=190)


# 函数参数默认值
# print中的end就是默认值参数
# 定义函数时通过形参名=值的形式，为参数指定一个默认值，调用时从写参数会覆盖默认值
# 带默认值的函数必须放在最后，或者说带默认值的参数之后都是默认值参数
# def greet(name,gender,age,height,msg='hello'):
#     print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')
#     print(f'我想说{msg}')
#
# greet('张三','男',18,172)
# greet('张三','男',18,172,'hehe')
# greet('张三','男',18,172,msg='hehe')


# 可变参数
# 可变位置参数，在定义时，在形参前面加上*，可以接收任意数量的位置参数，并打包成一个元组
def test1(*args):
    print(args)
    pass
test1('张三','男',18,172)
# 只能将位置参数传给args，可变关键字参数不能交给args
# 错误示例
#test1('张三','男',18,height=172)

# 可变关键字参数，在定义时，在形参前面加上两个**，可以接收任意数量的关键字参数，并打包成一个字典
def test2(**kwargs):
    print(kwargs)
    pass
test2(name='张三',gender='男',age=18,height=172)

# 可变位置参数，可变关键字参数，可以同时使用，但是必须先写可变位置参数
def test3(*args,**kwargs):
    print(args)
    print(kwargs)
    pass
test3('张三','男',age=18,height=172)

# 可变位置参数，可变关键字参数，也能与其他类型参数仪器使用
def test4(a,b,c='hello',**kwargs):
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print(a)
    print(b)
    print(c)
    print(kwargs)
    pass
test4('张三','男',c='你好',age=18,height=172)