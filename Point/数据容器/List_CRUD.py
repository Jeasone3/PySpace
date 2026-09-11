# 方法和函数：当一个函数隶属于一个对象时，称该函数时这个对象的方法
# 增加
nums = [10, 20, 30, 40]
# 1.通过append方法，在列表尾部追加一个元素
# nums.append(50)
# print(nums)

# 2.通过insert方法，在列表指定位置下标出添加一个元素
# nums.insert(2,666)
# print(nums)

# 3.通过extend方法，将可迭代对象的内容依次取出，追加到列表尾部
# nums.extend(range(1,3))
# print(nums)

# 删除
# 1.通过列表的pop方法删除指定位置的元素，并返回该元素
# result = nums.pop(1)
# print(nums)
# print(result)

# 2.通过列表的remove方法，删除列表中第一次出现的指定值
# nums.remove(10)
# print(nums)

# 3. 通过clear方法，删除列表中所有的元素
# nums.clear()
# print(nums)

# 4.通过del关键字，删除指定元素
# del nums[1]
# print(nums)

# 修改
# nums[1] = 99
# print(nums)

# 查询
print(nums[1])