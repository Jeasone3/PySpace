# 定义元组
# t1 = (28,29,10,39)
# t2 = ('北京','上海','你好')
# t3 = (100,True,'你好',None)
# t4 = (100,30,20,'你好',True)
# print(type(t1),t1)
# print(type(t2),t2)
# print(type(t3),t3)
# print(type(t4),t4)

# 元组的元素不能修改，但是如果使元组中嵌套列表，可以修改列表的元素
# t1 = (100,20,30,20,[10,20,30])
# t1[4][1] = 1
# print(t1)

# 定义空元组
# t1 = ()
# t2 = tuple()

# 定义只有一个元素的元组
# t0 = ('e') # 会认为元组多余
# t1 = ('e'
#       '你好') # 拼字符串
# # 加 ，
# t3 = ('你好',)
# t4 = ('e',)
# print(t1)


# 常用方法
# index
# t1 = (28, 77, 65, 99, 99)
# res = t1.index(28)
# print(res) # 0


#count : 统计元素出现的次数
# ret = t1.count(99)
# print(ret)


# 内置函数
# max
# t1 = (23, 44, 56, 77, 98,19)
# print(max(t1))
#
# # min
# print(min(t1))
#
# # len
# print(len(t1))
#
# # sorted
# print(sorted(t1))
# print(sorted(t1, reverse=True))
#
# # sum
# print( sum(t1) )

# 实际中的元组不一定是我们定义的，比如函数的可变参数 *args 就是一个元组
# def demo(*args):
#     print(args)
#     return sum(args)
#
# print(demo(1, 2, 3, 4))
#

# 循环遍历
index = 0
t1 = (1, 2, 4, 6, 7)
while index < len(t1):
    print(t1[index])
    index = index + 1

for item in t1:
    print(item)



