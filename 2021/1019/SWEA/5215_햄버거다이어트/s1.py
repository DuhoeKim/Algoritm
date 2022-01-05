import sys
sys.stdin = open("sample_input.txt")

def comb(s, total, kal):
    global result

    if kal > M:
        return

    result = max(result, total)


    for j in range(s, N):
        comb(j+1, total+info[j][0], kal+info[j][1])

T=int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    used = [0]*N
    info = []
    for _ in range(N):
        T, K = map(int, input().split())
        info.append([T, K])

    result = 0
    for i in range(N):
        comb(i+1, info[i][0], info[i][1])

    print('#{} {}'.format(test_case, result))