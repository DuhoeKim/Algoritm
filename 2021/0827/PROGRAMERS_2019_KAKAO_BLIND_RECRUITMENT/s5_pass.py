def solution(food_times, k):
    food_times_cnt = dict()
    kind_of_cnt = sorted(list(set(food_times)))

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

    temp_N = N
    skip = 0
    before_time = 0

    for cnt in kind_of_cnt:
        if not k // (temp_N*(cnt-before_time)):
            skip += k//temp_N
            k %= temp_N
            break
        else:
            k -= (cnt-before_time)*temp_N
            skip = cnt
            before_time = cnt
            temp_N -= food_times_cnt.get(cnt, 0)

    for i in range(N):
        if food_times[i] - skip > 0:
            k -= 1
            if k == -1:
                return i + 1

print(solution([1,5], 3))