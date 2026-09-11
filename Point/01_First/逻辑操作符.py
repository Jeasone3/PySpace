# and用于判断两侧的值，是否为True

print(True and True)
print(True and False)
print(False and False)

# and具备逻辑短路的能力
print(False and 3/0)

# and返回的不一定是布尔值，他返回的是某个参与计算的值的本身
print(2-2 and True)
print('' and True)
print(True and 8/2)

# or两侧是否至少有一个为True(只要有一个True，那就返回True)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# or同样具有逻辑短路的能力
print(True or 3/0)


# not用于取反
print(not True)
print(not False)

