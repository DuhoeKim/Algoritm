import sys
sys.stdin = open('input.txt')


def in_order(n):
    if n:                                               # n이 0이 아니면 (= 현재노드가 존재하면)
        in_order(left[n])                               # 왼쪽 트리로 들어가기 (인자로 왼쪽 자식)
        print(word[n], end='')                          # 현재 노드 출력
        in_order(right[n])                              # 오른쪽 트리 들어가기 (인자로 오른쪽 자식)

for test_case in range(1, 11):                          # 10번 반복

    N = int(input())                                    # 노드 갯수
    infomation = [input().split() for _ in range(N)]    # 정점 정보

    word = [0]*(N+1)                                    # 단어 저장
    left = [0]*(N+1)                                    # 왼쪽 자식
    right = [0]*(N+1)                                   # 오른 자식


    idx = 0                                             # 인덱스 초기화
    for info in infomation:
        for i in range(len(info)):
            if i == 0:                                  # 첫 글자는 노드 번호
                idx = int(info[i])                      # 인덱스 번호에 등록

            elif info[i].isdigit():                     # 숫자면 left, right에 넣기
                if not left[idx]:                       # 왼쪽에 숫자 있는지 확인
                    left[idx] = int(info[i])            # 왼쪽에 숫자 넣기
                else:
                    right[idx] = int(info[i])           # 오른쪽에 숫자 넣기

            else:
                word[idx] = info[i]                     # 단어 넣기

    print('#{} '.format(test_case), end='')             # 문제번호 출력
    in_order(1)                                         # 중위순회 시작
    print()                                             # 줄바꿈
