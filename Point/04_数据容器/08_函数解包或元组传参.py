
# * 起到打包的作用：
def test(*data):
    print(*data)
    print(type(data))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
test(list1)
test(tuple1)
test(*list1) # 调用时* 起到解包的作用
