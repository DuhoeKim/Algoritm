import sys
sys.stdin = open("sample_input.txt")

# Lomuto-partition
def partition(L, p, r):
    x = L[r]
    i = p-1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1

def quick_sort(L, start, end):
    if start < end:
        s = partition(L, start, end)
        quick_sort(L, start, s-1)
        quick_sort(L, s+1, end)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N-1)

    print('#{} {}'.format(test_case, numbers[N//2]))