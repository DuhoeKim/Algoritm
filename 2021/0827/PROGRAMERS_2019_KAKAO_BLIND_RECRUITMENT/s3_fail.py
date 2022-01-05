def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    N = len(food_times)
    b = 0
    while k >= N:
        k -= N
        b += 1
        N = N - (food_times.count(b))

    for i in range(len(food_times)):
        if food_times[i] - b > 0:
            k -= 1
            if k == -1:
                return i + 1
print(solution([3, 1, 2], 5))