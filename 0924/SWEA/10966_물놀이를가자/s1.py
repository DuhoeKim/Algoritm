import sys
from collections import deque
sys.stdin = open("sample_input.txt")

def is_it_possible(x, y):
    if 0 <= x < M and 0 <= y < N and mat[y][x] == 'L':
        return True
    return False

T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())

    mat = [input() for _ in range(N)]

    shortcut = [[N*M]*M for _ in range(N)]

    Q = deque([])
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 'W':
                shortcut[i][j] = 0
                Q.append([i, j])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while Q:
        y, x = Q.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if is_it_possible(nx, ny) and shortcut[ny][nx] > (shortcut[y][x]+1):
                shortcut[ny][nx] = shortcut[y][x] + 1
                Q.append([ny, nx])

    total = 0
    for row in shortcut:
        total += sum(row)

    print('#{} {}'.format(test_case, total))