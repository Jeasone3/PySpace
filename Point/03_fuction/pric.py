
def clac_total(*args):
    """
    计算总运动量
    :param args: 每一天运动量
    :return: 总运动量
    """
    return sum(args)

def clac_avg(total, days = 7):
    """
    计算平均值
    :param total: 运动总量
    :param days: 天数
    :return: 平均值
    """
    return total / days

def check_success(total, goal = 120):
    if total > goal:
        return '恭喜挑战成功'
    else:
        return '挑战失败'

def main(title, duration):
    print(f'{title}{duration},挑战赛(请输入每天数量)')
    num1 = int(input('第一天'))
    num2 = int(input('第二天'))
    num3 = int(input('第三天'))
    num4 = int(input('第四天'))
    num5 = int(input('第五天'))
    num6 = int(input('第六天'))
    num7 = int(input('第七天'))
