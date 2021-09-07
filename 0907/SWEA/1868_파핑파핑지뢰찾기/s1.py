from pprint import pprint
import sys
sys.stdin = open('input.txt')

def is_mine (r, c):                                                     # 지뢰인지 검사하는 함수
    if (0 <= r < N) and (0 <= c < N) and (mat[c][r] == '*'):            # 범위 안에 있고 지뢰면 True 반환
        return True
    return False                                                        # 지뢰 아니면 Flase 반환

def is_zero (x, y):                              # 0인지 검사하는 함수
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]             # 좌상 상 우상 좌 우 좌하 하 우하
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]             # 좌상 상 우상 좌 우 좌하 하 우하

    for direction in range(8):                   # 8방향 검사
        nx = x + dx[direction]
        ny = y + dy[direction]

        if is_mine(nx, ny):                      # 8방향 내에 지뢰있으면 False 반환
            return False
    return True                                  # 0 이면 True 반환

def change_dot_to_num(x, y):
    mat[y][x] = 0
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]            # 좌상 상 우상 좌 우 좌하 하 우하
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]            # 좌상 상 우상 좌 우 좌하 하 우하

    for drct in range(8):                       # 8방향 검사
        temp_cnt = 0
        nx = x + dx[drct]
        ny = y + dy[drct]

        if (0 <= nx < N) and (0 <= ny < N) and mat[ny][nx] == '.':                  # . 이면 숫자로 변환하기
            for direction in range(8):                                              # 8방향 검사
                nnx = nx + dx[direction]
                nny = ny + dy[direction]

                if is_mine(nnx, nny):                                               # 8방향 내에 지뢰있으면 temp += 1
                    temp_cnt += 1
            mat[ny][nx] = temp_cnt                                                  # 검사 끝나면 숫자로 변환
            if mat[ny][nx] == 0:                                                    # 0이면 다시 8방향 변환 ㄱㄱ
                change_dot_to_num(nx, ny)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    mat = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == '.' and is_zero(j, i):            # . 이고 0이면
                change_dot_to_num(j, i)                       # 주변 .을 모두 숫자로 바꾸는 함수 실행
                cnt += 1                                      # 클릭 수 +1

    for i in range(N):
        for j in range(N):
            if mat[i][j] == '.':                              # 나머지 숫자가 아닌 .을 찾아서 클릭!!
                cnt += 1
    print('#{} {}'.format(test_case, cnt))