from collections import deque
import sys
sys.stdin = open("sample_sample_input.txt")

def calc(op, n1, n2, f):
    if op == 1:
        return f+' + {}'.format(n2), n1 + n2
    elif op == 2:
        return f+' - {}'.format(n2), n1 - n2
    elif op == 3:
        return f+' * {}'.format(n2), n1 * n2
    elif op == 4:
        return f+' / {}'.format(n2), n1 // n2

def calc2(n1, n2, f):
    formular = (f + '{}'.format(n2)).split()
    L = len(formular)
    total = int(formular[0])


    for i in range(1, L, 2):
        if formular[i] == '+':
            total += int(formular[i+1])
        elif formular[i] == '-':
            total -= int(formular[i+1])
        elif formular[i] == '*':
            total *= int(formular[i+1])
        else:
            if int(formular[i+1]):
                total //= int(formular[i+1])

    return f+'{}'.format(n2), total

T = int(input())
for test_case in range(1, T+1):
    N, O, M = map(int, input().split())

    can_touch = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input())

    checked = [0]*1000

    result = M
    if W in can_touch:
        result = 1
    else:
        Q = deque([])
        for i in range(N):
            Q.append([str(can_touch[i]), can_touch[i], 1])
            checked[can_touch[i]] = 1

        while Q:
            form, num, cnt = Q.popleft()
            for t in can_touch:
                temp_form2, temp2 = calc2(num, t, form)
                if 0 <= temp2 <= 999 and cnt+2 < result and cnt+2 < M and not checked[temp2]:
                    checked[temp2] = 1
                    if temp2 != W:
                        Q.append([temp_form2, temp2, cnt+1])
                    else:
                        if len(temp_form2.split()) == cnt:
                            result = min(result, cnt+1)
                        else:
                            result = min(result, cnt+2)

                for o in operators:
                    if t == 0 and o == 4:
                        continue
                    temp_form, temp = calc(o, num, t, form)
                    if 0 <= temp <= 999 and cnt+3 < result and cnt+3 < M and not checked[temp]:
                        checked[temp] = 1
                        if temp != W:
                            Q.append([temp_form, temp, cnt + 2])
                        else:
                            result = min(result, cnt+3)

    print(result)