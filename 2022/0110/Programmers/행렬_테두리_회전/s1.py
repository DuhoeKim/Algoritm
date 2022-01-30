def solution(rows, columns, queries):
    answer = []
    mat = [[num + (columns*r) for num in range(1, columns+1)] for r in range(rows)]
    print(mat)
    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]

    for query in queries:

        for i in range(4):
            query[i] = query[i] - 1

        r1, c1, r2, c2 = query
        r, c = r1, c1

        initial = mat[r1][c1]

        temp = initial
        temp2 = initial
        min_num = initial

        direction = 0

        while True:
            nr = r + dr[direction]
            nc = c + dc[direction]

            if (r1 > nr) or (nr > r2) or (c1 > nc) or (c2 < nc):
                direction = (direction + 1) % 4
                continue

            min_num = min(mat[nr][nc], min_num)

            if mat[nr][nc] == initial:
                mat[nr][nc] = temp
                break

            else:
                temp = mat[nr][nc]
                mat[nr][nc] = temp2
                temp2 = temp
                r, c = nr, nc

        answer.append(min_num)
    return answer

# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))
print(solution(3, 6, [[1, 1, 2, 2]]))