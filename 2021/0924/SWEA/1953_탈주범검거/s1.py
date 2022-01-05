from collections import deque
import sys
sys.stdin = open("sample_input.txt")

def is_connected(c, r, way):
    '''
    터널이 연결되어 있는지 확인하는 함수

    :param c: 현재 x좌표 (현재 열)
    :param r: 현재 y좌표 (현재 행)
    :param way: 이전 터널 진행 방향
    :return: boolean type
    '''
    if 0 <= c < M and 0 <= r < N and not visited[r][c]:         # 범위 안에 있고, 방문한적 없는지 검사
        if (way + 2) % 4 in tunnel[mat[r][c]]:                  # (이전 터널 진행방향+2)%4 가 현재 터널에 있다면 연결가능
            return True
    return False

tunnel = [[],                                                   # 터널의 모양 정보
          [0, 1, 2, 3],                                         # 터널의 번호에 맞게 인덱스 설정
          [0, 2],                                               # 각 터널에 뚫려 있는 방향 저장.
          [1, 3],
          [0, 1],
          [1, 2],
          [2, 3],
          [0, 3],
          ]

T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]   # 지하 지도
    visited = [[0]*M for _ in range(N)]                         # 지하 크기와 같은 방문 표시 및 시간 표시

    manhole = [R, C]                                            # 맨홀 위치 = 시작점

    Q = deque([])                                               # 큐 생성
    Q.append(manhole)

    visited[R][C] = 1                                           # 시작점 시간 1로 초기화

    dx = [0, 1, 0, -1]                                          # 델타 상 우 하 좌 순서
    dy = [-1, 0, 1, 0]

    while Q:                                                    # 큐가 빌때 까지 BFS
        y, x = Q.popleft()
        shape_of_tunnel = tunnel[mat[y][x]]                     # 현재 위치에서 터널이 어느 방향으로 뚫려 있는지 모양 정보 받아오기

        if visited[y][x] < L:                                   # 현재 이동 시간이 L 보다 작을 때만 탐색. (같거나 클 경우 다음 터널로 가지 못하므로)

            for direction in shape_of_tunnel:                   # 갈수 있는 방향만 순회
                nx = x + dx[direction]
                ny = y + dy[direction]

                if is_connected(nx, ny, direction):             # 연결 되었는지 확인
                    Q.append([ny, nx])                          # 다음 칸 큐에 추가
                    visited[ny][nx] = visited[y][x] + 1         # 다음 칸 방문 표시 및 시간 기록


    result = 0                                                  # 결과 초기화
    for i in range(N):                                          # 배열 순회
        for j in range(M):
            if visited[i][j]:                                   # 방문한 곳이면 범인이 있을 수 있는 곳
                result += 1

    print('#{} {}'.format(test_case, result))