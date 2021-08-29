import sys
sys.stdin = open('input.txt')

T = int(input())
answer = []
for test_case in range(1, T+1):

    N, M, K = map(int, input().split())

    coming_time = list(map(int, input().split()))           # 손님오는 시간 입력
    coming_time.sort(reverse=1)                                      # 시간 순서로 정렬

    result = 'Possible'                                     # 결과 초기화

    for i in range(N):
        fish_bun = K * (coming_time[i] // M) - (N-i)        # 붕어빵 수 = (현재 시간) // (붕어빵 만드는데 걸리는 시간) * (만드는 붕어빵 수) - (왔다 간 사람 수)
                                                            # 이때, 왔다 간 사람 수는 현재 손님을 포함하여 (현재 인덱스 +1) 이다.

        if fish_bun < 0:                                    # 남은 붕어빵 수가 음수면
            result = 'Impossible'                           # 불가능!
            break                                           # 순회 멈춰!
    answer.append('#{} {}'.format(test_case, result))
print('\n'.join(answer))