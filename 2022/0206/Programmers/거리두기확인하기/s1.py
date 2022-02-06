def solution(places):
    answer = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for place in places:
        flag = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    Q = [(i, j)]
                    t = 0
                    visited = [[0]*5 for _ in range(5)]
                    while Q and t < 2:
                        r, c = Q.pop(0)
                        visited[r][c] = 1
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5 or visited[nr][nc]:
                                continue
                            if place[nr][nc] == "O":
                                Q.append((nr, nc))
                            elif place[nr][nc] == "P":
                                flag = 1
                                break
                        t += 1
                        if flag:
                            break
                if flag:
                    break
            if flag:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer