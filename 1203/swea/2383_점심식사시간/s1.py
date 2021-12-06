import sys
sys.stdin = open("sample_input.txt")

def calc_minimum_time(sf, ss):
    global minimun_time
    if len(sf) > 2:
        for i in range(3, len(sf)):
            sf[i] += max(0, stair_info[0][-1]-(sf[i] - sf[i-3]))
    if len(ss) > 2:
        for j in range(3, len(ss)):
            ss[j] += max(0, stair_info[1][-1]-(ss[j] - ss[j-3]))

    if len(ss) and len(sf):
        minimun_time = min(minimun_time, max(sf[-1], ss[-1]))
    elif len(ss) == 0:
        minimun_time = min(minimun_time, sf[-1])
    elif len(sf) == 0:
        minimun_time = min(minimun_time, ss[-1])

def division_people(i, first, second):
    global M

    if i == M:
        sorted_first = sorted(first)
        sorted_second = sorted(second)
        calc_minimum_time(sorted_first, sorted_second)
        return

    for s in range(2):
        total_time = abs(people_info[i][0] - stair_info[s][0]) + abs(people_info[i][1] - stair_info[s][1]) + stair_info[s][-1] + 1
        if not s:
            first.append(total_time)
            division_people(i + 1, first, second)
            first.pop()
        else:
            second.append(total_time)
            division_people(i + 1, first, second)
            second.pop()

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 사람, 계단찾기
    stair_info = []
    people_info = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] > 1:
                stair_info.append([i, j, mat[i][j]])
            elif mat[i][j] == 1:
                people_info.append([i, j])

    M = len(people_info)
    minimun_time = 200
    division_people(0, [], [])

    print('#{} {}'.format(test_case, minimun_time))