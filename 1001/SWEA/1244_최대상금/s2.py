import sys
sys.stdin = open("input.txt")
'''
상백님 풀이 참조
'''
def find_maximum(numbers, now_cnt):
    global maximum
    N = len(numbers)
    if now_cnt == 0:
        now_cash = int(''.join(numbers))
        if now_cash >= maximum:
            maximum = now_cash
        return

    for i in range(N):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            now_cash = int(''.join(numbers))
            if not visited.get((now_cash, now_cnt-1)):          # 처음에 생각하지 못했던 가지치기 부분 : 상백님 풀이 덕분에 해결
                visited[(now_cash, now_cnt-1)] = True
                find_maximum(numbers, now_cnt-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]



T = int(input())
for test_case in range(1, T+1):
    cards, cnt = input().split()

    cards = list(cards)
    cnt = int(cnt)

    maximum = 0

    visited = dict()
    find_maximum(cards, cnt)
    print('#{} {}'.format(test_case, maximum))