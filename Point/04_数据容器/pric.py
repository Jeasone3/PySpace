
print('请输入学生成绩,输入“结束”停止:')

sorce_list = []

while True:
    data = input('请输入学生成绩')
    if data == '结束':
        break
    else:
        sorce_list.append(int(data))

if sorce_list:
    avg = sum(sorce_list)/len(sorce_list)

    pass_count = 0
    excellent_count = 0
    for item in sorce_list:
        if item >= 60:
            pass_count += 1
        if item >= 90:
            excellent_count += 1
    pass_rate = pass_count / len(sorce_list)*100
    excellent_rate = excellent_count / len(sorce_list)*100

    print(f'总人数为：{len(sorce_list)}')
    print(f'最高分{max(sorce_list)}')
    print(f'最低分{min(sorce_list)}')
    print(f'合格人数{pass_count}')
    print(f'优秀人数{excellent_count}')
    print(f'优秀率{excellent_rate:.1f}')
    print(f'平均成绩:{pass_rate:.2f}%')

else:
    print("成绩表为空")