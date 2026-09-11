
"""
# range(0,10) 0-10 左闭右开
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

#加密文件
text = input('请输入你要加密的文件')
secret = ''
for i in text:
    secret += chr(ord(i) + 1)
    pass
print(f'经过加密后的内容为{secret}')



secret = input('请输入你要加密的文件')
for i in secret:
    text += chr(ord(i)-1)
    pass
print(f'经过解密的内容为{text}')



