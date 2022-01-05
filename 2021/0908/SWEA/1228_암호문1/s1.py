import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):

    L = int(input())
    origin = list(map(int, input().split()))
    C = int(input())
    commend = input().split()

    i = 0
    for _ in range(C):
        if commend[i] == 'I':
            i += 1
            index = int(commend[i])
            i += 1
            num_insert = int(commend[i])
            i += 1
            for _ in range(num_insert):
                origin.insert(index, commend[i])
                index += 1
                i += 1
    print('#{} '.format(test_case), *origin[:10])


