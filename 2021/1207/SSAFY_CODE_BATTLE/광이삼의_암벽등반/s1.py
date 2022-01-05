import sys
sys.stdin = open("sample_input.txt")

def DFS(r, c, m, cnt):
    global result

    # 출발지일 때, 결과 비교
    if mat[r][c] == 2:
        result = min(result, cnt)
        return

    # 더 이상 이동 불가능할 때,
    # 혹은 현재 고리 사용 갯수가 최소 갯수보다 같거나 클 때,
    # 탐색 중지
    if m == 0 or (cnt >= result):
        return

    # 4방향 탐색
    for d in range(4):
        nr = r + dy[d]
        nc = c + dx[d]

        # 범위 안에 있고, 방문한 적이 없으면 이동
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = 1     # 다음칸 방문처리

            # 다음 칸이 고리 일 때,
            if mat[nr][nc] == 1:
                for _ in range(2):
                    if _:
                        # 고리 걸기
                        DFS(nr, nc, L, cnt + 1)  # 이동 가능거리 초기화, 고리 + 1
                        visited[nr][nc] = 0     # 방문이 끝나면 방문 처리 초기화
                    else:
                        # 고리 안걸기
                        DFS(nr, nc, m-1, cnt)  # 이동 가능거리 감소, 고리 그대로
                        visited[nr][nc] = 0    # 방문이 끝나면 방문 처리 초기화

            # 고리가 아닐 때
            else:
                DFS(nr, nc, m-1, cnt)   # 이동 가능거리 감소
                visited[nr][nc] = 0     # 방문이 끝나면 방문 처리 초기화

T = int(input())
for test_case in range(1, T+1):
    M, N, L = map(int, input().split())
    # 고리 정보 입력
    mat = [list(map(int, input().split())) for _ in range(M)]

    # 방문 기록 배열
    visited = [[0]*N for _ in range(M)]
    
    # 출발지 찾기
    gi, gj = 0, 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 3:
                gi = i
                gj = j

    # 출발지 초기화
    visited[gi][gj] = 1

    # 델타 (상 우 하 좌)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 결과를 최대 고리 갯수보다 많게 초기화
    result = 10

    # DFS 탐색
    DFS(gi, gj, L, 0)   # 출발지 좌표, 현재 이동 가능 횟수, 현재 고리 사용 갯수
    
    # 도착하지 못했다면 -1로 변경
    if result == 10:
        result = -1

    print('#{} {}'.format(test_case, result))