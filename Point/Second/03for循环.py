
"""
range(0,10) 0-10 左闭右开
# 这个n在for外面定义，可以超出range的值，因为进入for之后n会被初始化为range左边的值
n = 5

for n in range(10):
    print('你好',n)

for  n in 'abcdef':
    print(n)
    pass

nums = [1,2,3,4]
for i in nums:
    print(i)
    pass
"""

# 不要在循环内部修改可迭代对象 ,否则会导致死循环  ！！！
nums = [1,2,3,]
for i in nums:
    nums.append(4)
    print(i)

#
# 加密文件
# text = input('请输入你要加密的文件')
# secret = ''
# for i in text:
#     secret += chr(ord(i) + 1)
#     pass
# print(f'经过加密后的内容为{secret}')




# secret = input('请输入你要加密的文件')
# for i in secret:
#     text += chr(ord(i)-1)
#     pass
# print(f'经过解密的内容为{text}')

