from itertools import combinations
import sys
sys.stdin = open("sample_input.txt")

'''
모듈 사용 풀이
'''
def cook(arr, N):
    M = N//2
    total = 0
    # 2가지 재료의 맛 궁합 더하기
    for i in range(M-1):
        for j in range(i+1, M):
            total += mat[arr[i]][arr[j]]
            total += mat[arr[j]][arr[i]]
    return total

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ingredient = [num for num in range(N)]

    result = 98754321
    # checked = []

    for comb in combinations(ingredient, N//2):
        # if list(comb) in checked:
        #     continue

        A = list(comb)
        B = []
        for i in ingredient:
            if i not in comb:
                B.append(i)
        # checked.append(B)

        A_score = cook(A, N)
        B_score = cook(B, N)
        temp = abs(A_score - B_score)
        result = min(result, temp)

    print('#{} {}'.format(test_case, result))