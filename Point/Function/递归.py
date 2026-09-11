# def welcome(n):
#     print(f'你好啊{n}')
#     if n>1:
#         welcome(n-1)
#
# welcome(5)

# 递归顺序相反
# def welcome(n):
#     if n>1:
#         welcome(n-1)
#     print(f'你好啊{n}')
#
# welcome(5)

# 应用re
# def factorial(num):
#     if num < 0:
#         return '请输入正整数'
#     if num == 0:
#         return 1
#     return num * factorial(num-1)
# print(factorial(3))

# 函数的说明文档
def add(n1, n2):
    """
    计算两数之和
    :param n1:第一个加数
    :param n2: 第二个加数
    :return: 和
    """
    return n1 + n2
print(add(3,4))
