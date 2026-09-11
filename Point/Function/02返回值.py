# # None 是一个特殊的字面量。表示：空值/无值/无意义
# # 就是void
# msg = None
#
# # None 的类型是NoneType
# print(type(msg))
#
# # None 转为布尔值是False
# print(bool(msg))
# if not msg:
#     print('你好')
#     pass


# 不能进行数学运算，也不能进行字符拼接
# result1 = msg + 1
# result1 = msg + 'hello'


def add(n1,n2):
    return n1 + n2
result = add(100,200)
print(result)

# print没有返回值
