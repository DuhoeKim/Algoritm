import sys
sys.stdin = open("sample_input.txt")

# 중위 순회
def inorder(i, N):                                  # 현재 인덱스와 N 을 인자로 받는다.
    global now_num                                  # 글로벌 변수 : 현재 추가할 숫자
    
    if i <= N:                                      # 현재 인덱스가 N이하 이고,
        inorder(2*i, N)                             # 왼쪽 탐색
        bin_tree_arr[i] = now_num                   # 현재 인덱스를 현재 숫자로 변경
        now_num += 1                                # 현재 숫자에 +1
        inorder(2*i+1, N)                           # 오른쪽 탐색

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    bin_tree_arr = [0]*(N+1)

    now_num = 1                                     # 트리에 채울 숫자 초기화
    inorder(1, N)                                   # 중위순회 시작

    print('#{} {} {}'.format(test_case, bin_tree_arr[1], bin_tree_arr[N//2]))