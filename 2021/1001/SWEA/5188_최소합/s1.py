from collections import deque
import sys
sys.stdin = open("sample_input.txt")

def is_valid(r, c, nr, nc):
    if 0 <= nr < N and 0 <= nc < N and mat[nr][nc]+shortcut[r][c] < shortcut[nr][nc]:
        return True
    return False

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    
    shortcut = [[987654321]*N for _ in range(N)]    # 최소 표시용
    dx = [0, 1]                                     # 델타 아래, 오른쪽
    dy = [1, 0]
    Q = deque([])                                   # 빈큐 생성

    Q.append([0, 0])                                # 시작좌표 Q 에 담기
    shortcut[0][0] = mat[0][0]                      # 시작 지점 초기화

    while Q:                                        # BFS
        i, j = Q.popleft()

        for d in range(2):                          # 2 방향 델타 탐색
            ni = i + dy[d]
            nj = j + dx[d]

            if is_valid(i, j, ni, nj):
                Q.append([ni, nj])
                shortcut[ni][nj] = mat[ni][nj] + shortcut[i][j]

    print('#{} {}'.format(test_case, shortcut[-1][-1]))