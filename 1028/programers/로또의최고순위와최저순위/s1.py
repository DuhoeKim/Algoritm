def solution(lottos, win_nums):
    answer = []
    prize_num = [6, 6, 5, 4, 3, 2, 1]
    zero_cnt = 0
    now_cnt = 0
    for i in range(6):
        if lottos[i] in win_nums:
            now_cnt += 1
        elif lottos[i] == 0:
            zero_cnt += 1
    answer.append(prize_num[now_cnt + zero_cnt])
    answer.append(prize_num[now_cnt])
    return answer