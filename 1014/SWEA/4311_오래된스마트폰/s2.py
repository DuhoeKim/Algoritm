import sys
sys.stdin = open("sample_sample_input.txt")

def comb(num):
    if len(num) == 3:
        return
    for i in range(N):
        touch_list.append(num+str(can_touch[i]))
        if num+str(can_touch[i]) != '0':
            comb(num+str(can_touch[i]))

def calc(op, n1, n2, c):

    c += len(n2)+1

    if op == 1:
        return int(n1)+int(n2), c
    if op == 2:
        return int(n1)-int(n2), c
    if op == 3:
        return int(n1)*int(n2), c
    if op == 4:
        return int(n1)//int(n2), c



def DFS(n, cnt):
    global result

    if int(n) == W:
        if n in touch_list:
            result = min(result, cnt)
        else:
            result = min(result, cnt+1)
        return

    for num in touch_list:
        if num == '0':
            continue
        for o in operators:
            n_n, n_c = calc(o, n, num, cnt)
            if 0 <= n_n <= 999 and n_c < M and n_c < result and n_c < checked[n_n]:
                checked[n_n] = n_c
                DFS(str(n_n), n_c)

T = int(input())
for test_case in range(1, T+1):
    N, O, M = map(int, input().split())

    can_touch = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input())

    touch_list = []
    comb('')

    checked = [987654321]*1000

    result = 987654321
    for num in touch_list:
        DFS(num, len(num))

    if result == 987654321:
        result = -1

    print('#%d %d'%(test_case, result))