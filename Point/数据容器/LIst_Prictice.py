print('请输入学生成绩，输入“结束”停止录入')
score_list = []
while True:
    data = input('请输入学生成绩')
    if data == '结束':
        break
    else:
        score_list.append(int(data))


# excellent_person  = 0
# pass_person = 0
# for index in range(len(score_list)):
#     if score_list[index] >= 90:
#         excellent_person += 1
#     if score_list[index] >= 60:
#         pass_person += 1
# avg = sum(score_list) / len(score_list)
# pass_rate = pass_person / len(score_list)
# excellent_rate = excellent_person / len(score_list)

if score_list:
    avg = sum(score_list) / len(score_list)
    pass_count = 0
    excellent_count = 0
    for item in score_list:
        if item >= 60:
            pass_count += 1
        if item >=90:
            excellent_count += 1
    pass_rate = pass_count / len(score_list) * 100
    excellent_rate = excellent_count / len(score_list) * 100

    print(f'总人数：{len(score_list)}')
    print(f'最高分：{max(score_list)}')
    print(f'最低分：{min(score_list)}')
    print(f'合格人数：{pass_count}')
    print(f'合格率：{pass_rate:.1f}')
    print(f'优秀人数：{excellent_count}')
    print(f'优秀率：{excellent_rate:.1f}')
    print(f'平均分数：{avg:.1f}')

else:
    print('成绩表为空')
