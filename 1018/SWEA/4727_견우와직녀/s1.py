from pprint import pprint
import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    shortcut = [[[987654321]*N for _ in range(N)] for _ in range(2)]

    shortcut[0][0][0] = 0
    shortcut[1][0][0] = 0

    Q = [[0, 0, 0, 0]]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c, is_used, time = Q.pop(0)

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                next_time = shortcut[is_used][nr][nc]
                next_used = is_used

                if mat[nr][nc]:
                    next_time = time + (mat[nr][nc] - time % mat[nr][nc])

                elif not is_used and not mat[nr][nc]:
                    next_time = time + (M - time % M)
                    next_used = 1

                if next_time < shortcut[next_used][nr][nc]:
                    shortcut[next_used][nr][nc] = next_time
                    Q.append([nr, nc, next_used, next_time])

    print('#{} {}'.format(test_case, min(shortcut[0][-1][-1], shortcut[1][-1][-1])))