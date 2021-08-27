def solution(food_times, k):
    food_times_cnt = dict()

    total = 0
    N = 0
    for time in food_times:
        if food_times_cnt.get(time):
            food_times_cnt[time] += 1
        else:
            food_times_cnt[time] = 1
        total += time
        N += 1
    if total <= k:
        return -1

    rec = 0
    sub_N = N
    while k >= sub_N:
        k -= sub_N
        rec += 1
        sub_N -= food_times_cnt.get(rec, 0)

    for i in range(N):
        if food_times[i] - rec > 0:
            k -= 1
            if k == -1:
                return i + 1

print(solution([3, 1, 2], 5))