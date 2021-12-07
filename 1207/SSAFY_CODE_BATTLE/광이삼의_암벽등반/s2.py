import sys
sys.stdin = open("sample_input.txt")

def DFS(r, c, cnt):
    global result

    # 도착지까지 갈 수 있는지 검사
    if abs(r - si)+abs(c - sj) <= L:
        result = min(result, cnt)
        return

    # 가지치기
    if cnt >= result:
        return
    
    # 고리들을 검사
    for ring in rings:
        nr, nc = ring   # 다음으로 갈 고리 위치
        
        # 다음 고리에 방문한 적 없고, 갈 수 있는 거리가 되면 이동
        if not visited[nr][nc] and (abs(nr - r) + abs(nc - c) <= L):
            visited[nr][nc] = 1     # 방문 처리
            DFS(nr, nc, cnt+1)      # 이동 => 고리 갯수 +1
            visited[nr][nc] = 0     # 돌아왔다면 방문 처리 해제

T = int(input())
for test_case in range(1, T+1):
    M, N, L = map(int, input().split())
    # 고리 정보 입력
    mat = [list(map(int, input().split())) for _ in range(M)]

    # 방문 기록 배열
    visited = [[0]*N for _ in range(M)]

    
    # 출발지, 도착지, 고리 찾기
    si, sj = 0, 0
    gi, gj = 0, 0
    rings = []
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 2:
                si = i
                sj = j
            elif mat[i][j] == 1:
                rings.append([i, j])
            elif mat[i][j] == 3:
                gi = i
                gj = j

    # 도착지 방문처리 (도착지부터 역으로 탐색하기 위해)
    visited[gi][gj] = 1

    # 결과를 최대 고리 갯수보다 많게 초기화
    result = 10

    # DFS 탐색(도착지 부터 출발지로 탐색하기) : 도착하지 못하는 경우를 빠르게 캐치하기 위해서
    DFS(gi, gj, 0)   # 도착지 좌표, 현재 고리 사용 갯수

    # 갈 수 없으면 결과 -1로 변경
    if result == 10:
        result = -1

    print('#{} {}'.format(test_case, result))