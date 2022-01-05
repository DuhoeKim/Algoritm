from collections import deque
def solution(food_times, k):
    n = len(food_times)
    if k <= n :
        rest = k % n
        if not rest:
            for i in range(n):
                if not food_times[i]:
                    return i+1
            else:
                return -1
        else:
            for i in range(n):
                if not food_times[i]:
                    rest -= 1
                    if rest== -1:
                        return i
            else:
                return -1
    else:
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
print(solution([3, 1, 2], 6))