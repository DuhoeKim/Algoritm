import sys
sys.stdin = open("sample_input.txt")

def combination(start, N, L):

    # 불필요한 중복을 막기 위한 가지치기
    if len(food_comb)*2 == L:               # (모든 경우의 수 / 2) 만큼 구했으면 더 이상 탐색 X
        return

    # N/2 개 골랐으면 나눠담기
    if sum(used) == N//2:
        A = []
        B = []
        for i in range(N):
            if used[i]:
                A.append(i)
            else:
                B.append(i)
        food_comb.append([A, B])

    for i in range(start, N):
        if not used[i]:
            used[i] = 1
            combination(i+1, N, L)
            used[i] = 0

def cook(arr, N):
    M = N//2
    total = 0
    # 2가지 재료의 맛 궁합 더하기
    for i in range(M-1):
        for j in range(i+1, M):
            total += mat[arr[i]][arr[j]]
            total += mat[arr[j]][arr[i]]
    return total

# 조합의 가지 수를 구하기 위한 팩토리얼 함수. (memoization 방식)
def factorial(n):
    if memo[n]:
        return memo[n]
    else:
        return factorial(n-1)*n

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # (조합의 가지 수)/2 구하기
    memo = [0]*(N+1)
    memo[0] = 1
    x = factorial(N)
    y = factorial(N//2)
    limit = x//y**2

    # 음식 조합 구하기
    food_comb = []
    used = [0]*N
    combination(0, N, limit)

    # 결과 초기화
    result = 987654321

    # 각 요리 합 계산 후 차 구하기
    for comb in food_comb:
        A, B = comb
        A_score = cook(A, N)
        B_score = cook(B, N)
        temp = abs(A_score - B_score)
        result = min(result, temp)

    print('#{} {}'.format(test_case, result))