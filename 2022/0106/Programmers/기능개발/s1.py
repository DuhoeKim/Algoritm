def solution(p, s):
    answer = []
    checked = [0] * len(p)
    for i in range(len(p)):
        if (100 - p[i]) % s[i]:
            checked[i] = ((100 - p[i]) // s[i]) + 1
        else:
            checked[i] = (100 - p[i]) // s[i]

    cnt = 1
    point = checked[0]
    for i in range(len(checked)-1):
        point = max(checked[i], point)
        if point >= checked[i+1]:
            cnt += 1
        else:
            answer.append(cnt)
            point = checked[i+1]
            cnt = 1

    answer.append(cnt)
    return answer