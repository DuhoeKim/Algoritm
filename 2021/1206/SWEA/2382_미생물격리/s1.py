import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    before = [[0]*N for _ in range(N)]
    after = [[0]*N for _ in range(N)]

    direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


    for _ in range(K):
        i, j, k, d = map(int, input().split())
        before[i][j] = (k, d, 0)

    # M번 반복
    for _ in range(M):

        for i in range(N):
            for j in range(N):
                if before[i][j]:
                    k, d, nk = before[i][j]
                    nk, nd, mk = 0, 0, 0
                    ni = i + direction[d][0]
                    nj = j + direction[d][1]

                    if 0 < ni < N-1 and 0 < nj < N-1:
                        if after[ni][nj]:
                            nk, nd, mk = after[ni][nj]
                        else:
                            nd = d
                        nk = nk + k
                        if k > mk:
                            nd = d
                            mk = k
                    else:
                        nk = k//2
                        mk = nk
                        if nk:
                            if d == 1:
                                nd = 2
                            elif d == 2:
                                nd = 1
                            elif d == 3:
                                nd = 4
                            elif d == 4:
                                nd = 3
                    if nk:
                        after[ni][nj] = (nk, nd, mk)

        for i in range(N):
            arr = after[i]
            before[i] = arr[:]
            after[i] = [0]*N

    result = 0
    for i in range(N):
        for j in range(N):
            if before[i][j]:
                result += before[i][j][0]

    print('#{} {}'.format(test_case, result))