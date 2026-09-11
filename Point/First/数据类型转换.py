# 数据类型转换

# 把指定数据转化为字符串   任何类型都可以转化位字符串类型
result1 = str(18)
print(type(result1), result1)

# 把指定类型转化为整型
print(int(15.6))

# 把指定数据转化为浮点型：float（）
print(float(18))
print(float('78'))

# 使用 == 来判断左右两侧是否相等
a = 5
b = 7
c = '5'

result = a == c
# == 的两侧类型要一致
print(result)

# 通过ord()来判断Unicode编码
print(ord('我'))
print(ord('a'))

# 通过chr()将Unicode编码转化为字符
print(chr(97))

# string比较大小时比较的就是Unicode编码类似strcmp

# if（string有交集，看strlen谁长谁大）
msg1 = 'abc'
msg2 = 'abcdef'
print(msg1 > msg2)

# boolean类型
print(bool(1))
print(bool(0))
print(bool(''))

