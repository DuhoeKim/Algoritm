def solution(grid):
    answer = []
    direction = {
        'L': [(0, -1, 2), (0, 1, 3), (1, 0, 1), (-1, 0, 0)],
        'R': [(0, 1, 3), (0, -1, 2), (-1, 0, 0), (1, 0, 1)],
        'S': [(-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3)]
    }

    init = []
    routes = []
    row = 0
    col = 0

    for r in grid:
        row += 1
        col = len(r)
        temp = []
        for _ in r:
            temp.append([0, 0, 0, 0])
        init.append(temp)

    for d in range(4):
        temp = []
        for r in init:
            tmp = []
            for _ in r:
                tmp.append([0, 0, 0, 0])
            temp.append(tmp)
        sr, sc, next_direction = 0, 0, d
        cnt = 0

        while True:
            if not temp[sr][sc][next_direction]:
                temp[sr][sc][next_direction] = 1
            else:
                if temp not in routes:
                    routes.append(temp)
                    answer.append(cnt)
                break
            cnt += 1
            dr, dc, next_direction = direction[grid[sr][sc]][next_direction]
            sr = sr + dr
            sc = sc + dc
            if sr < 0:
                sr = row - 1
            elif sr >= row:
                sr = 0

            if sc < 0:
                sc = col - 1
            elif sc >= col:
                sc = 0
    return sorted(answer)

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))
