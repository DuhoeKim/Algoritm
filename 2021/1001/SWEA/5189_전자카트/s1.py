import sys
sys.stdin = open("sample_input.txt")

def DFS(i, visited, now_usage):
    global min_usage

    # 0번을 제외하고 다른 곳을 모두 방문했다면 0번으로 가기
    if len(visited) == N-1:
        now_usage += mat[i][0]
        if now_usage < min_usage:
            min_usage = now_usage
            return

    # 다음 방문할 곳 정하기
    for j in range(1, N):                       # 0번을 제외한 나머지 방 순회
        if (j == i) or (j in visited):          # 현재 행이거나 방문 했다면 스킵
            continue

        if now_usage + mat[i][j] < min_usage:   # 현재까지 사용량 + 다음 소모량이 최소 사용량보다 작을 때만 방문
            temp = now_usage + mat[i][j]        # 임시변수에 사용량 저장
            visited.append(j)                   # 방문처리
            DFS(j, visited, temp)               # 다음 방 방문하기
            visited.pop()                       # 나오면 방문처리 지우기


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 최소 사용량 초기화 과정
    min_usage = 0
    for row in mat:
        min_usage += sum(row)

    managed = []
    total_usage = 0
    DFS(0, managed, total_usage)

    print('#{} {}'.format(test_case, min_usage))