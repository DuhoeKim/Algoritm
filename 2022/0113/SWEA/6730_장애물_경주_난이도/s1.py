import sys
sys.stdin = open('s_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    up = 0
    down = 0
    for i in range(N-1):
        if (arr[i+1] - arr[i]) > 0:
            up = max(arr[i+1]-arr[i], up)
        else:
            down = max(-1*(arr[i+1]-arr[i]), down)

    print('#{} {} {}'.format(test_case, up, down))