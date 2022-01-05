from collections import deque
def solution(food_times, k):
    ft = deque([num for num in range(len(food_times))])
    while k:
        k -= 1
        idx = ft.popleft()
        food_times[idx] -= 1
        if food_times[idx]:
            ft.append(idx)
        else:
            if not len(ft):
                return -1
    return ft[0] + 1

print(solution([3, 1, 2], 5))