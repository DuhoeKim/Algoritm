def solution(grid):
    answer = []
    direction = {
        'L': [2, 3, 1, 0],
        'R': [3, 2, 0, 1],
        'S': [0, 1, 2, 3]
    }
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    init = []
    row = 0
    col = 0

    for r in grid:
        row += 1
        col = len(r)
        temp = []
        for _ in r:
            temp.append([0, 0, 0, 0])
        init.append(temp)


    for r in range(row):
        for c in range(col):
            sr, sc = r, c
            for d in range(4):
                next_direction = d
                cnt = 0

                while True:
                    if not init[sr][sc][next_direction]:
                        init[sr][sc][next_direction] = 1
                    else:
                        if sr == r and sc == c and cnt:
                            answer.append(cnt)
                        break
                    cnt += 1
                    sr = sr + dr[next_direction]
                    sc = sc + dc[next_direction]

                    if sr < 0:
                        sr = row - 1
                    elif sr >= row:
                        sr = 0

                    if sc < 0:
                        sc = col - 1
                    elif sc >= col:
                        sc = 0

                    next_direction = direction[grid[sr][sc]][next_direction]
    return sorted(answer)

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))
