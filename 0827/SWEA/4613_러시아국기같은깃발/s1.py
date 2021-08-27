import sys
sys.stdin = open('sample_input.txt')


def WBR(temp_total, col):

    for i in range(1, col-1):                               # 하얀색이 차지할 수 있는 경우의 수 중 하나 고르기 :1줄~(세로-2)줄
        temp_sum = 0                                        # 임시합 저장
        for cnt_white_line in range(i):                     # 현재 고른 경우의 수 만큼 흰색 칠하기
            for letter1 in mat[cnt_white_line]:             # 0 ~ i-1 행 까지 W 아닌거 칠하기
                if letter1 != 'W':
                    temp_sum += 1                           # 합 누적
        if temp_sum > temp_total:                           # 누적한게 최소보다 크면 다음거 검사
            continue

        for j in range(1, col-i):                           # 파란색 칠할 수 있는 경우의 수 중 하나 고르기 : 1줄 ~ (세로 - 하얀색 칠한 줄 수(i) - 1)줄
            temp_sum2 = temp_sum                            # 하얀색까지 칠한  합 복사
            for cnt_blue_line in range(j):                  # 현재 고른 경우의 수 만큼 파란색 칠하기
                for letter2 in mat[cnt_blue_line+i]:        # i ~ i+(j-1) 행 까지 B 아닌거 칠하기
                    if letter2 != 'B':
                        temp_sum2 += 1                      # 합 누적
            if temp_sum2 > temp_total:                      # 누적한게 최소보다 크면 파란색 칠한거 초기화하고 다음 경우의 수 검사
                continue

            for cnt_red_line in range(col-i-j):             # 나머지 줄 수 다 칠하기 : (세로 - 하얀줄(i) - 파란줄(j))
                for letter3 in mat[cnt_red_line+j+i]:       # i + j 행 부터 끝까지
                    if letter3 != 'R':                      # R 아니면 칠하기
                        temp_sum2 += 1                      # 합 누적
            if temp_sum2 < temp_total:                      # 총합 검사: 총합이 최소 합보다 작으면
                temp_total = temp_sum2                      # 최소합을 현재 총합으로 갱신

    return temp_total                                       # 모든 경우의수 확인하고 최소합 반환


T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())                         # 깃발 크기 정보

    mat = [input() for _ in range(N)]                        # 현재 깃발모양

    max_total = N*M                                          # 최대 깃발색칠 횟수

    total = WBR(max_total, N)                                # 함수 실행 ( 최대 깃발 색칠횟수와, 세로 길이를 인자로)

    print('#{} {}'.format(test_case, total))