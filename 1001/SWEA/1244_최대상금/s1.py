import sys
sys.stdin = open("input.txt")

'''
전략 : 현재 인덱스 보다 뒤쪽에 큰 숫자가 있다면 교환. 없으면 다음 인덱스로 넘어가기

1) 현재 인덱스보다 뒤를 확인해서, 최댓값들의 인덱스번호를 리스트에 담는다.

2) 최댓값 인덱스 중 가장 마지막 인덱스보다 앞에 있는 요소 중, 현재 인덱스보다 작은 값(이하 smaller)의 갯수를 찾는다.

3) 현재 인덱스와 비교할 최대값 선택하기
    3-1) 최대값이 2개 이상일 때,
        3-1-1)  최댓값 중 뒤에서 smaller+1 번째에 있는 값을 선택한다.
                이때, smaller 의 갯수가 최댓값의 갯수를 벗어나면 최댓값 중 제일 앞에 있는 값을 선택한다.
                ex) 32777에서 현재 인덱스가 3을 가르킨다면, smaller 는 1개 이므로 뒤에서 두번째 7을 선택
        
        3-1-2) 만약 카운트가 한개 남았다면, 제일 뒤에 있는 최댓값 선택
    
    3-2) 최댓값이 한개일 때는 그것을 선택.
    
    
4) 선택된 최댓값과 현재값을 비교한다. 
    선택된 최댓값이 현재값 이상이면 교환하고, 카운트를 하나 깎는다. 

5) 카운트가 0이 되면 종료, 아니라면 다음 인덱스로 넘어간다.
    
6) 마지막 인덱스까지 확인하고도 카운트가 남았을 때,
    6-1) 현재 남은 카운트가 홀수일 때:
        5-1-1) 카드들 중 현재 뒤에서 두번째 카드와 같은 숫자가 여러장이라면 현재 상금값을 그대로 출력
        5-1-2) 뒤에서 두번째 카드가 한장이라면, 마지막 카드와 교환하고 출력
    
    6-2) 현재 남은 카운트가 짝수일 때:
        현재 상금값을 그대로 출력

'''

def find_max(num_list, now_cnt):
    N = len(num_list)

    for i in range(N-1):
        max_index = i+1
        max_index_list = []
        small_idx_cnt = 0

        for j in range(i+1, N):
            if num_list[j] > num_list[max_index]:
                max_index = j
                max_index_list = [j]
            elif num_list[j] == num_list[max_index]:
                max_index_list.append(j)

        for j in range(i+1, N):
            if j < max_index_list[-1] and num_list[i] > num_list[j]:
                small_idx_cnt += 1

        target_idx = (len(max_index_list)-1) - small_idx_cnt
        if now_cnt == 1:
            target_idx = len(max_index_list) -1

        if target_idx < 0:
            change_idx = max_index_list[0]
        else:
            change_idx = max_index_list[target_idx]

        if num_list[change_idx] >= num_list[i]:
            num_list[change_idx], num_list[i] = num_list[i], num_list[change_idx]
            now_cnt -= 1
            if now_cnt == 0:
                break
    else:
        if now_cnt % 2:
            if num_list.count(num_list[-2]) == 1:
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
    return int(''.join(num_list))


T = int(input())
for test_case in range(1, T+1):
    number, change = input().split()

    number = list(number)
    change = int(change)

    maximum = find_max(number, change)

    print('#{} {}'.format(test_case, maximum))