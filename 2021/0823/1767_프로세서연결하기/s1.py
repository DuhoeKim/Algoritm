import sys
sys.stdin = open('sample_input.txt')

"""
전략 :

경로를 2로 표시하자.
가장 자리 프로세서도 2로 바꿔놓자.

완전탐색으로 해볼까?
4**N ..? 음..

아.. 최대한 많은 코어를 연결하는거구나.. 그럼 음..

1. 가장 자리를 프로세서는 다 2로 바꾼다.

2. 프로세서 좌표를 뽑아서 리스트로 만든다.

3. 4**(프로세서 수) 만큼의 탐색을 시작한다.. (상,하,좌,우)

4. 한쪽 방향씩 검사하고 한 방향 검사 끝나면 다음 프로세서로 이동.
    이때 넘겨줘야 하는거, 현재까지 연결된 프로서세서 수, 전선길이.

5. 마지막 프로세서 검사가 끝나면 global 변수랑 비교해서 값 갱신
"""
def findWay(arr, processor, candidate, size, stack = [], cnt = 0, line = 0):

    global max_cnt, min_line

    # 현재 카운트 + 남은 후보군 < max_cnt 이면 종료
    if (cnt + candidate.count(0) < max_cnt) or (cnt + candidate.count(0) == max_cnt and line > min_line):
        return

    # 델타 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 차례대로 순회
    for i in range(len(processor)):

        # 이미 확인한 프로세스면 다음 확인
        if candidate[i] == 1:
            continue
        # 아니라면 1로 변경
        else:
            candidate[i] = 1

        # 현재 프로세서 좌표
        x, y = processor[i]

        # 사방탐색
        for direction in range(4):

            # 현재 좌표 복사
            nx, ny = x, y

            # 현재 카운트 복사
            temp_cnt = cnt
            temp_line = line

            # 전원이 연결됐는지 확인하는 토글
            power = 1

            # 범위를 벗어날 때까지 한칸씩 진행하며 확인하기
            while True:

                # 한칸 전진
                nx += dx[direction]
                ny += dy[direction]
                # 벗어났는지 확인
                if nx < 0 or nx >= size or ny < 0 or ny >= size:
                    break

                # 만약에 0이 아니면 토글 바꾸고 전진 멈추기
                if arr[ny][nx] != 0:
                    power = 0
                    break
                # 전진 하면 현재 경로 2로 바꾸고 전선길이 + 경로 저장
                else:
                    arr[ny][nx] = 2
                    temp_line += 1
                    stack.append([nx, ny])

            # 범위 벗어났을 때 전원 연결 됐는지 확인
            # 전원 연결 됐으면 프로세서 카운트 +1
            if power == 1:
                temp_cnt += 1
                # 만약 마지막 프로세서 였으면  global 이랑 비교
                if 0 not in candidate:
                    # 연결된 프로세서 수 크면 갱신
                    if temp_cnt > max_cnt:
                        max_cnt = temp_cnt
                        min_line = temp_line
                    # 같으면 전선길이 갱신
                    elif temp_cnt == max_cnt:
                        if temp_line < min_line:
                            min_line = temp_line

                # 마지막 아니면 다음거 검사
                else:
                    findWay(arr, processor, candidate, size, stack, temp_cnt, temp_line)

            # 전원 연결 안됐을 때
            else:
                # 만약 마지막 프로세서 였으면  global 이랑 비교
                if 0 not in candidate:
                    # 연결된 프로세서 수 크면 갱신
                    if temp_cnt > max_cnt:
                        max_cnt = temp_cnt
                        min_line = temp_line
                    # 같으면 전선길이 갱신
                    elif temp_cnt == max_cnt:
                        if temp_line < min_line:
                            min_line = temp_line

                # 마지막 아니면 다음거 검사
                else:
                    # 전원이 연결안됐으니 이전 카운트 정보를 그대로 넘겨준다.
                    findWay(arr, processor, candidate, size, stack, cnt, line)

            # 다음 방향 탐색 전 갔던 경로 지우기
            for _ in range(temp_line - line):
                nx, ny = stack.pop()
                arr[ny][nx] = 0

        # 사방탐색 끝나면 candidate 0으로 바꿔주기
        candidate[i] = 0


T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 가장자리 2로 바꾸기
    # 가장자리는 어차피 카운트에 무관함
    for i in range(N):
        if mat[0][i] == 1:
            mat[0][i] = 2
        if mat[i][0] == 1:
            mat[i][0] = 2
        if mat[N-1][i] == 1:
            mat[N-1][i] =2
        if mat[i][N-1] == 1:
            mat[i][N-1] = 2

    # 프로세서 좌표 모음 초기화
    all_p = []

    # 모든 프로세서 좌표 찾기
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                all_p.append([j, i])

    # 후보군 생성
    visited = [0] * len(all_p)

    # 최대 연결 수, 전선길이
    max_cnt = 0
    min_line = 0

    # 함수 실행
    findWay(mat, all_p, visited, N)
    print(min_line)