import sys
sys.stdin = open("sample_input.txt")

def check_and_switch(idx):
    '''
    현재 노드와 부모노드를 비교하여 교환여부를 판단하고, 교환하는 함수 
    '''
    
    if idx == 1:                                                                # 1번 노드는 무시                            
        return
    if tree_arr[idx] < tree_arr[idx//2]:                                        # 현재 노드가 부모노드보다 작으면
        tree_arr[idx], tree_arr[idx//2] = tree_arr[idx//2], tree_arr[idx]       # 교환
        check_and_switch(idx//2)                                                # 교환한 노드부터 다시 검사

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    num_list = list(map(int, input().split()))

    tree_arr = [0]*(N+1)                                                        # 노드 수만큼 배열 생성

    i = 1
    for num in num_list:                                                        # 차례로 트리에 넣기
        tree_arr[i] = num                                                       # 현재 노드자리에 숫자 넣기
        check_and_switch(i)                                                     # 교환여부 확인 및 교환
        i += 1                                                                  # 다음 노드로 옮기기

    total = 0                                                                   # 총합 초기화
    while N:                                                                    # 마지막 인덱스(N)//2 가 0이 될때까지 부모노드 더하기
        N //= 2
        total += tree_arr[N]

    print('#{} {}'.format(test_case, total))