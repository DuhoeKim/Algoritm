import sys
sys.stdin = open("sample_input.txt")

'''
전략 : 

다음 칸이 갈 수 없는 길이면 K 내에서 깎아보고 진행... 하면 되는거 아닌가?
GG... 
'''

def is_possible(x, y, r_s):                                                 # 갈 수 있는 길인지 판별하는 함수
    if 0<= x < N and 0<= y < N and [y, x] not in r_s:
        return True
    return False

T = int(input())
for test_case in range(1, T+1):

    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    start_candidate = []                                                    # 출발 후보지 구하기

    max_height = 0                                                          # 최대 높이 초기화
    for i in range(N):                                                      # 배열 순회
        for j in range(N):
            if mountain[i][j] > max_height:                                 # 더 높은 곳 찾았을 때
                start_candidate = []                                        # 이전까지 후보군 초기화 및 현재 좌표 추가
                start_candidate.append([i, j])
                max_height = mountain[i][j]
            elif mountain[i][j] == max_height:                              # 정상과 같은 높이를 찾았을 때
                start_candidate.append([i, j])                              # 후보군에 추가

    dx = [0, 0, -1, 1]                                                      # 델타 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]

    max_distance = 0                                                        # 최대길이 초기화

    for start in start_candidate:                                           # 출발지 차례대로 선정
        distance = 1                                                        # 현재까지거리
        diff = 0                                                            # 현재 지형이 파진 양 (배열 원본을 건드리지 않기위한 변수)
        dis_K_stack = [[distance, K, diff, -1]]                             # 현재칸의 거리, K, 파헤쳐진 양, 마지막으로 방문한 방향 을 기록하는 스택
        route_stack = [start]                                               # 왔던 길을 기록하는 스택
                                                                            # 스택을 둘로 나누어서 정보를 편하게 관리할 수 있다.
        
        while route_stack:                                                  # 스택이 없을 때까지 루프 진행
            y, x = route_stack.pop()                                        # 이전 좌표 불러오기
            now_distance, now_K, diff, last_direction = dis_K_stack.pop()   # 이전 좌표가 가지고 있는 정보 불러오기
            
            toggle = 1                                                      # 반복문을 제어하기 위한 토글    

            while toggle:   
                for direction in range(4):                                  # 4방 탐색
                    if direction <= last_direction:                         # 가본곳이면 스킵하기
                        continue
                    nx = x + dx[direction]                                  # 다음칸 좌표 설정
                    ny = y + dy[direction]

                    if is_possible(nx, ny, route_stack) and (mountain[ny][nx]-(mountain[y][x]-diff)) < now_K:       # 갈 수 있는 길이고, (다음칸 - 현재칸)이 now_k 보다 작을 때만 진행
                                                                                                                    # 이때, 현재칸 = 원래 높이 - 파헤쳐진 양
                        route_stack.append([y, x])                                                                  # 현재칸 좌표 및 정보 저장
                        dis_K_stack.append([now_distance, now_K, diff, direction])

                        if mountain[ny][nx]-(mountain[y][x]-diff) >= 0:                                             # 다음칸이 높거나 같으면
                            diff = mountain[ny][nx]-(mountain[y][x]-diff) + 1                                       # 얼마나 파헤쳤는지 저장
                            now_K = 0
                        else:
                            diff = 0                                                                                # 그렇지 않을경우 파헤쳐진양 0으로 초기화

                        x, y = nx, ny                                                                               # 다음칸으로 이동
                        now_distance += 1                                                                           # 이동거리 1 증가
                        last_direction = -1                                                                         # 마지막 방문 방향 초기화
                        break

                else:                                                       # 4방향 검사했는데 길이 없을 시,
                    if now_distance > max_distance:                         # 현재 거리와 최대거리 비교해서 갱신
                        max_distance = now_distance
                    toggle = 0                                              # 토글 0 으로 만들어서 반복끝내기

    print('#{} {}'.format(test_case, max_distance))