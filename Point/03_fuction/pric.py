
def test(*args, **kwargs):
    print(args,end='   ')
    print(kwargs)
    pass
test('张三','男',name = '张三', age = 19)