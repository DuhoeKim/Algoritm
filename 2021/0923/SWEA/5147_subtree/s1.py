import sys
sys.stdin = open("sample_input.txt")

# 전위순회 진행
def preorder(N):                 # N번째 노드를 인자로 받음
    global cnt                   # 글로벌 cnt 사용

    if N:
        cnt += 1                 # cnt +1
        preorder(left[N])        # 왼쪽 노드 방문
        preorder(right[N])       # 오른쪽 노드 방문

T = int(input())
for test_case in range(1, T+1):

    E, N = map(int, input().split())
    left = [0] * (E+2)                          # 왼쪽
    right = [0] * (E+2)                         # 오른쪽

    bridge = list(map(int, input().split()))

    for i in range(E):
        parent = bridge[2*i]                    # 부모노드
        child = bridge[2*i+1]                   # 자식노드

        if left[parent]:                        # 왼쪽 노드가 있으면
            right[parent] = child               # 오른쪽 노드에 저장
        else:                                   # 왼쪽 노드 없으면
            left[parent] = child                # 왼쪽 노드에 저장

    cnt = 0
    preorder(N)                                 # N 번 노드부터 전위순회 진행
    print('#{} {}'.format(test_case, cnt))