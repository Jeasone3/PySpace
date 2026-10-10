# 备注:所有列表方法都作用当前层，不会深入里层
# 列表常用方法
# 1.列表.index(值),不会进入嵌套列表中查找
# fruits = ['香蕉','苹果','橙子','香蕉']
# result = fruits.index('香蕉')
# print(result)

# 2. count方法，统计某个元素在列表中出现的次数，返回值时元素出现次数的下标,同样不会统计嵌套列表
# 没有元素返回0
# nums = [10,20,10,40,10,60]
# result = nums.count(10)
# print(result)

# 3.reverse 方法，对列表进行反转
# nums = [11, 22, 33, 44]
# nums.reverse()
# print(nums)

# sort方法对列表进行排序，若想从大到小，将reverse参数设为True
# nums = [22, 55, 33, 99]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# 若列表中既有数字又有字符串，无法使用sort进行排序

# 若列表中都是字符串，就会按照首字母的Unicode 编码大小排序

