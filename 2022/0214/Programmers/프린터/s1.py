def solution(priorities, location):
    answer = 0
    p_cnt = [0] * 10
    for p in priorities:
        p_cnt[p] += 1

    while True:
        now_prio = priorities.pop(0)
        for p in range(now_prio+1, 10):
            if p_cnt[p]:
                priorities.append(now_prio)
                break
        else:
            answer += 1
            p_cnt[now_prio] -= 1
            if location == 0:
                return answer
        if location > 0:
            location -= 1
        else:
            location = len(priorities)-1