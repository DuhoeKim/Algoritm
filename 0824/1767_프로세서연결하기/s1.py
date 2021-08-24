import sys
sys.stdin = open('sample_input.txt')

"""
천천히 해보자.

1. 가장 자리를 제외한 프로세서 탐색하기
2. 앞에서부터 순서대로 탐색하고 표시하기
3. 우선 전선을 놓을 수 있는지 확인하기
4. 전선을 놨으면 1로 바꾸기
"""

# 전선이 연결될 수 있는지 확인하는 함수
# 전선이 연결되면 연결된 길이를 리턴하고, 그렇지 않으면 None 을 리턴한다.
def connecting(now_x, now_y, direction, arr, size):
    # 델타 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 다음 좌표부터 계산하기 위해 한칸 이동
    now_x += dx[direction]
    now_y += dy[direction]
    line_cnt = 0 # 연결한 전선길이 초기화

    # 범위를 벗어날 때까지 (= 전원이 연결될 때까지) 반복하기
    while 0 <= now_x < size and 0 <= now_y < size:
        # 현재 칸이 0이면 경로를 1로 바꾸고 전선길이 +1
        if arr[now_y][now_x] == 0:
            arr[now_y][now_x] = 1
            line_cnt += 1
        # 0이 아니라면 None 리턴 (=전선 연결 x)
        else:
            return
        # 다음칸 확인을 위해 전진
        now_x += dx[direction]
        now_y += dy[direction]
    # while 문 내에 return에 걸리지 않고 범위를 벗어났으면 전원이 연결된 것이므로
    # 전선 길이를 리턴
    return line_cnt

# 이전 까지 지도, 지도 크기, 현재까지 연결된 프로세서 수, 현재 연결된 전선길이, 현재 확인하고 있는 프로세서 번호
def dfs(m, n, now_cnt, now_line, p_idx):

    # 글로벌 변수 활용
    global cnt, min_line

    # 만약에 프로세서를 모두 확인했다면
    # 현재까지 카운트한 프로세서수가 기존 연결된 프로세서수보다 많은지 검사
    # 같다면 전선길이가 짧은지 검사
    if p_idx == len(processor):
        if now_cnt > cnt:
            cnt = now_cnt
            min_line = now_line
        elif now_cnt == cnt:
            if now_line < min_line:
                min_line = now_line
        return
    # 현재까지 연결한 프로세서 수 + 남은 프로세서 수가 최다 연결 프로세서 수보다 작으면 검사하지 않고 빠져나감
    elif now_cnt + len(processor)-p_idx < cnt:
        return
    # 현재까지 연결한 프로세서 수 + 남은 프로세서 수가 최다 연결 프로세서 수와 같은데,
    # 현재 전선길이가 같거나 크면 검사하지 않고 빠져나감
    # (전선이 더 길어질 가능성 존재)
    elif now_cnt + len(processor)-p_idx == cnt and now_line >= min_line:
        return

    # 프로세서 좌표 받아오기
    x, y = processor[p_idx]

    # 현재 프로세서에서 4방향 검사하기
    for delta in range(4):
        # 지도 복사
        m2 = [r[:] for r in m]
        # 현재 방향으로 갔을 때 연결 길이 검사
        temp_line = connecting(x, y, delta, m2, n)
        # 연결된 길이가 존재하면 (= 전원이 연결되었으면)
        if temp_line:
            # 전선이 깔린 지도, 지도크기, 현재 연결된 프로세서 수 + 1, 현재 전선길이 + 연결된 전선길이, 다음 프로세서 인덱스 를 인자로 넘겨주어 다음 프로세서 확인
            dfs(m2, n, now_cnt+1, now_line+temp_line, p_idx+1)
        # 연결이 안되었으면
        else:
            # 현재 상태 그대로 유지하고, 다음 프로세서로 넘어가기
            dfs(m, n, now_cnt, now_line, p_idx+1)


T = int(input())
for test_case in range(1, T+1):

    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    # 프로세서 추리기
    processor = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if mat[i][j] == 1:
                processor.append([j, i])

    # 연결 프로세서랑 라인 초기화
    cnt = 0
    min_line = N**2

    dfs(mat, N, 0, 0, 0)

    print('#{} {}'.format(test_case, min_line))