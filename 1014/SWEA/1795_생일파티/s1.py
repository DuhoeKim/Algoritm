from collections import deque
import sys
sys.stdin = open("input.txt")

'''
전략 : 길을 역으로 찾는다 x 에서 출발 -> 가장 오래 걸리는 집 찾기
        
        이때, 길의 정보를 반대로 입력한다. 1 -> 4 까지 10 이면 저장할 때 4 -> 1 10 으로 저장.
'''
T = int(input())
for test_case in range(1, T+1):
    N, M, X = map(int, input().split())
    
    # 올 때 사용할 그래프, 갈 때 사용할 그래프
    graph1 = [[0]*(N+1) for _ in range(N+1)]
    graph2 = [[0]*(N+1) for _ in range(N+1)]
    
    # 0번 인덱스 : X 까지 가는데 걸리는 최소 시간, 1번 인덱스 : 돌아올 때 걸리는 최소 시간
    shortcut = [[10000*100, 10000*100]for _ in range(N+1)]
    shortcut[0] = [0, 0]
    shortcut[X] = [0, 0]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph1[y][x] = c                     # X 로 올때를 계산할 그래프 정보를 반대로 입력
        graph2[x][y] = c                     # X 에서 돌아갈 때 그래프
    
    # 큐 생성 및 초기화
    Q = deque([X])

    # 올 때 시간 계산
    while Q:
        now = Q.popleft()

        for next in range(N+1):
            if graph1[now][next] and graph1[now][next] + shortcut[now][0] < shortcut[next][0]:
                shortcut[next][0] = graph1[now][next] + shortcut[now][0]
                Q.append(next)
    
    # 큐 다시 초기화
    Q.append(X)
    
    # 갈 때 시간 계산
    while Q:
        now = Q.popleft()

        for next in range(N+1):
            if graph2[now][next] and graph2[now][next] + shortcut[now][1] < shortcut[next][1]:
                shortcut[next][1] = graph2[now][next] + shortcut[now][1]
                Q.append(next)
    
    # 결과 뽑기
    result = sum(max(shortcut, key=lambda x: sum(x)))

    print('#{} {}'.format(test_case, result))