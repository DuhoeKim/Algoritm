T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    scores = set()

    scores.add(0)
    for i in range(N):
        temp = set(scores)
        for num in temp:
            scores.add(num + arr[i])

    result = len(scores)
    print('#{} {}'.format(test_case, result))