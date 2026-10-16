# 字符串下标
msg = 'hello eeee'
# print(msg[0])
# print(msg[1])
# print(msg[2])

# 字符串中的字符不能进行修改
# msg[0] = 'a'


# 常用的方法
# index
print(msg.index('e'))

# split
m1 = 'hello@eeee@Jeason'
print(m1.split('@'))

# replace
print(msg.replace('hello','good'))

# count 统计指定字符串在原字符串出现的次数
print(msg.count('ee'))

# strip 方法：从某个字符串中删除，指定字符串中的任意字符
# 从两侧删除，直到遇到第一个不在字符串中的字符就停下来
# 实际中常用的是为了去除空格
massage1 = '66eee666eeee666'
print(massage1.strip('6'))