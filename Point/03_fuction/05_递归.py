# 使用递归打印n次'你好啊'
# def welcome(n):
#     print(f'你好啊{n}')
#     if n>1:
#         welcome(n-1)
#
# welcome(5)

# 递归顺序相反(从大到小)
# def welcome(n):
#     if n>1:
#         welcome(n-1)
#     print(f'你好啊{n}')
#
# welcome(5)


# 应用return
def factorial(num):
    if num < 0:
        return '请输入正整数'
    if num == 0:
        return 1
    return num * factorial(num-1)
print(factorial(3))
