import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):                                  # 10 번 반복

    N = int(input())                                            # 배열크기 입력
    mat = [list(map(int, input().split())) for _ in range(N)]   # 배열 입력

    mat_T = [list(col) for col in zip(*mat)]                    # 전치행렬 만들기 (=행을 열로 열을 행으로)

    mode = 0                                                    # 자석이 짝을 지었는지 확인하기 위한 토글
    cnt = 0                                                     # 자석쌍의 합 초기화

    for row in mat_T:                                           # 전치행렬의 행을 차례로 순회
        for num in row:                                         # 행의 요소를 순회

            if num == 1 and mode == 0:                          # 현재 요소가 N극이고, 이전에 N극을 찾은 적이 없으면
                mode = 1                                        # 모드를 1로 변경 (=N극을 찾았다는 표시)

            elif num == 2 and mode == 1:                        # 형재 요소가 S극이고, 이전에 N극이 있었다면
                cnt += 1                                        # 자석 쌍 수 누적
                mode = 0                                        # 모드를 다시 0으로 바꾸어 새로운 N극을 찾기

        mode = 0                                                # 행순회가 끝나면 모드를 초기화

    print('#{} {}'.format(test_case, cnt))                      # 결과 출력