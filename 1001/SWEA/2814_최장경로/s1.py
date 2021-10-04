import sys
sys.stdin = open("sample_input.txt")

def get_distance(now_node, now_distance):
    global distance

    visited[now_node] = 1                                               # 현재 노드 방문처리
    
    for next_node in range(1, N+1):                                     # 다음 노드 선정
        if graph[now_node][next_node] and not visited[next_node]:       # 연결 되어있고 방문안한 노드 찾기
            get_distance(next_node, now_distance + 1)                   # 노드 방문

    if now_distance > distance:                                         # 방문할 노드가 없다면 거리 비교
        distance = now_distance
    visited[now_node] = 0                                               # 방문 초기화

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]     # 그래프 생성

    visited = [0]*(N+1)                         # 방문 표시 초기화
    
    for _ in range(M):                          # 간선 정보 입력
        i, j = map(int, input().split())
        graph[i][j] = 1                         # 무향 그래프이기 때문에 양 방향 입력
        graph[j][i] = 1

    distance = 0                                # 거리 초기화
    for i in range(1, N+1):
        get_distance(i, 1)                      # 1번 노드부터 탐색 시작, 시작 거리 1

    print('#{} {}'.format(test_case, distance))