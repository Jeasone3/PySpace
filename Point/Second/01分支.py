# age = int(input('请输入你的年龄'))
# if age >= 18:
#     print('你是成年人')
# else:
#     print('你是未成年')
#
# # 多分支
# if age <= 10:
#     print('你是幼儿')
# elif age <= 18:
#     print('你是青少年')
# elif age <= 30:
#     print('你是青年')
# elif age <= 50:
#     print('你是中年')
# elif age<=60:
#     print('你是中老年')
# else:
#     print('你是老年')

# 嵌套分支
age = int(input('请输入你的年龄：'))
has_report = input('你是否提交了体检报告？（是/否）')
level = int(input('请输入你的会员等级（1/2/3）'))

if 18 <=age<=45:
    print('您的年龄符合比赛要求')
    if has_report == '是':
        print('您已提交体检报告')
        print('您可以参加比赛')
        if level == 1:
            print(f'尊敬的{level}会员，比赛结束后您可以获得纪念品T恤一件')
        elif level == 2:
            print(f'尊敬的{level}会员，比赛结束后您可以获得专业跑鞋一双')
        elif level == 3:
            print(f'尊敬的{level}会员，比赛结束后您可以获得运动耳机一副')
    elif has_report == '否':
        print('您未提交体检报告不能参加比赛')
    else:
        print('您提交的体检报告有误')
else:
    print('您的年龄不符合比赛要求')
