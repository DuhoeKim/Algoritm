from collections import deque
import sys
sys.stdin = open("input.txt")

def is_valid(i, j, ni, nj):
    return 0 <= ni < N and 0 <= nj < N and shortcut[i][j] + mat[ni][nj] < shortcut[ni][nj]

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    # 모든 칸의 복구시간 정보 입력
    mat = [list(map(int, ' '.join(input()).split())) for _ in range(N)]

    # 최소 이동 시간 기록용 배열 생성
    shortcut = [[987654321] * N for _ in range(N)]

    # 첫번째 칸은 출발지의 복구시간으로 초기화
    shortcut[0][0] = mat[0][0]

    # 델타
    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]

    # 큐 생성 및 초기화
    Q = deque([[0, 0]])

    # BFS
    while Q:
        r, c = Q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if is_valid(r, c, nr, nc):
                shortcut[nr][nc] = shortcut[r][c] + mat[nr][nc]
                Q.append([nr, nc])
    
    # 도착지 정보 출력
    print('#{} {}'.format(test_case, shortcut[-1][-1]))