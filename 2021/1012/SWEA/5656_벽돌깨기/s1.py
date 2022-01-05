from collections import deque
from copy import deepcopy
import sys
sys.stdin = open("sample_input.txt")

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 경계조건 + 다음 블록 확인
def is_valid(nr, nc, arr):
    return 0 <= nr < H and 0 <= nc < W and arr[nr][nc] and not checked[nr][nc]

# 현재 블록들, 공이 때리는 블록좌표, 남은 공수 를 인자로 받음
def breaking_bricks(filed, coordinate, remain_ball):
    global result

    # 남은 공체크
    if not remain_ball:
        temp = 0
        for row in range(H):
            for col in range(W):
                if filed[row][col]:
                    temp += 1
        if temp < result:
            result = temp
        return

    # 부술 벽돌 체크(bfs)
    r, c = coordinate
    Q = deque()
    Q.append([r, c])
    checked[r][c] = 1

    while Q:
        y, x = Q.popleft()
        M = filed[y][x]

        for t in range(1, M):
            for direction in range(4):
                ny = y + t*dy[direction]
                nx = x + t*dx[direction]

                if is_valid(ny, nx, filed):
                    Q.append([ny, nx])
                    checked[ny][nx] = 1

    # 벽돌제거
    temp_mat = deepcopy(filed)          # 원본을 유지하기 위해 deepcopy 사용
    for row in range(H):
        for col in range(W):
            if checked[row][col]:
                temp_mat[row][col] = 0
                checked[row][col] = 0

    # 벽돌정렬
    for row in range(H-1, 0, -1):
        for col in range(W):
            if not temp_mat[row][col]:
                for up in range(1, row+1):
                    if temp_mat[row-up][col]:
                        temp_mat[row][col], temp_mat[row-up][col] = temp_mat[row-up][col], temp_mat[row][col]
                        break

    # 남은 공 쏘기
    flag = 0    # 남은 블록이 없는 경우를 체크하기 위한 flag
    for nj in range(W):
        for ni in range(H):
            if temp_mat[ni][nj]:
                flag = 1
                breaking_bricks(temp_mat, [ni, nj], remain_ball-1)
                break
    if not flag:
        result = 0
        return

T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]
    checked = [[0]*W for _ in range(H)]

    result = W*H

    # 공쏘기
    for j in range(W):
        for i in range(H):
            if mat[i][j]:
                breaking_bricks(mat, [i, j], N)
                break

    print('#{} {}'.format(test_case, result))