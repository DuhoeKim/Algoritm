import sys
sys.stdin = open("input.txt")


def postorder(idx):

    if idx:                                                 # idx가 0이 아니면 후위순회 진행
        left_value = postorder(left[idx])                   # 왼쪽 방문
        right_value = postorder(right[idx])                 # 오른쪽 방문

        if V[idx] == '+':                                   # 사칙연산 처리
            return left_value + right_value
        elif V[idx] == '-':
            return left_value - right_value
        elif V[idx] == '*':
            return left_value * right_value
        elif V[idx] == '/':
            return left_value/right_value

        else:                                               # 현재 인덱스가 숫자인경우 그대로 리턴
            return V[idx]


T = 10
for test_case in range(1, T+1):

    N = int(input())


    V = [0]*(N+1)                                                       # 각 정점에 들어갈 값
    left = [0]*(N+1)                                                    # 각 정점의 왼쪽 자식 
    right = [0]*(N+1)                                                   # 각 정점의 오른쪽 자식


    for _ in range(N):                                                  # 정점개수만큼 정보입력받기
        info = input().split()

        if len(info) == 4:                                              # 정보의 길이가 4면
            node_num, value, left_node, right_node = info               # 노드번호, 값, 좌, 우 자식 입력
            V[int(node_num)] = value
            left[int(node_num)] = int(left_node)
            right[int(node_num)] = int(right_node)

        else:                                                           # 정보의 길이가 2면
            node_num, value = info                                      # 노드번호, 값 만 입력
            V[int(node_num)] = int(value)

    result = int(postorder(1))                                          # 루트(1번)부터 후위순회, 마지막 int로 변환하여 버림처리
    print('#{} {}'.format(test_case, result))