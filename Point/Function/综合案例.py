def clac_total(*args):
    return sum(args)

def clac_avg(total,days = 7):
    return total/days

def check_success(total,goal=120):
    if total >= goal:
        return '恭喜挑战成功'
    else:
        return '挑战失败'

def main(title,duration,goal):
    print(f'{title}{duration},挑战赛(请输入每天数量)：')
    num1 = int(input('第一天'))
    num2 = int(input('第二天'))
    num3 = int(input('第三天'))
    num4 = int(input('第四天'))
    num5 = int(input('第五天'))
    num6 = int(input('第六天'))
    num7 = int(input('第七天'))
    total = clac_total(num1,num2,num3,num4,num5,num6,num7)

    result = check_success(total,goal)

    print(f'{title}{duration},运动总结：')
    print(f'总数{total},平均值{clac_avg(total):.1f}')
    print(result)

main('俯卧撑',7,goal=4)