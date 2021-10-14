def find_set(x):
    if sets[x] == x:
        return x
    return find_set(sets[x])

def union(n1, n2):
    r1 = find_set(n1)
    r2 = find_set(n2)
    sets[r2] = r1

def get_num_of_sets(arr):
    count = [0]*(N+1)
    for i in range(1, N+1):
        if sets[i] == i:
            count[i] = 1
    return sum(count)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    sets = [num for num in range(N+1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    result = get_num_of_sets(sets)

    print('#{} {}'.format(test_case, result))