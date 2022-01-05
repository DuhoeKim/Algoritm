import sys
sys.stdin = open("sample_input.txt")

def postorder_sum(i, N):
    '''
    후위순회로 합을 채워가는 함수
    '''

    if i <= N:                                              # 현재 인덱스가 N 이하일 때
        if tree_arr[i] == 0:                                # 현재 인덱스 값이 0이면 후위순회 진행
            left_child = postorder_sum(2 * i, N)
            right_child = postorder_sum(2 * i + 1, N)
            tree_arr[i] = left_child + right_child
        return tree_arr[i]                                  # 현재 인덱스 값 리턴
    
    else:                                                   # 인덱스 범위 밖이면 0을 리턴                                               
        return 0

T = int(input())
for test_case in range(1, T+1):

    N, M, L = map(int, input().split())

    tree_arr = [0]*(N+1)

    for _ in range(M):
        V, num = map(int, input().split())
        tree_arr[V] = num

    postorder_sum(1, N)

    print('#{} {}'.format(test_case, tree_arr[L]))