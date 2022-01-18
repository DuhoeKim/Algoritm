def solution(dirs):
    answer = 0
    mat = [[""]*11 for _ in range(11)]
    sr, sc = 5, 5

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    d_lst = ["U", "L", "D", "R"]

    for d in dirs:
        nr = sr + dy[d_lst.index(d)]
        nc = sc + dx[d_lst.index(d)]

        if nr < 0 or nr > 10 or nc < 0 or nc > 10:
            continue

        if not mat[nr][nc].count(d):
            answer += 1
            mat[nr][nc] += d
            mat[sr][sc] += d_lst[((d_lst.index(d))+2) % 4]

        sr, sc = nr, nc
    return answer