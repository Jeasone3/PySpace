
print('欢迎来到:答题闯关挑战赛(输入q可以随时退出)\n')

ques1, ans1 = 'Python中用于输出的函数是?', 'print'
ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是？', 'and'
ques3, ans3 = 'Python是编译型还是解释型', '解释型'

TRY_MAX = 3
TOTAL_LEVELS = 3
is_gaming = True

for level in range(1,4):
    print(f'*******第{level}关********')
    if level == 1:
        question, answer = ques1,ans1
    elif level == 2:
        question, answer = ques2,ans2
    else:
        question, answer = ques3, ans3
        pass

    tries = 1
    while tries <= TRY_MAX:
        user_ans = input(question)
        if user_ans == answer:
            print('恭喜你答对了')
            break
        elif user_ans == ' ':
            continue
        elif user_ans == 'q':
            print('您已退出游戏')
            is_gaming = False
            break
        else :
            if TRY_MAX - tries > 0:
                print(f'回答错误，请从新作答您还剩{TRY_MAX - tries}')
                tries+=1
                continue
            else:
                print(f'挑战失败，本题的答案是{answer}，游戏结束')
                is_gaming = False
                break

    if not is_gaming:
        break
    print('恭喜您，成功通关所有关卡')