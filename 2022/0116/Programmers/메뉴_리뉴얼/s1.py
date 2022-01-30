from itertools import combinations
def solution(orders, course):
    answer = []

    for course_cnt in course:
        tmp = dict()
        candidates = []
        for order in orders:

            if len(order) < course_cnt:
                continue

            for comb in combinations(order, course_cnt):
                comb = ''.join(sorted(comb))
                if tmp.get(comb):
                    tmp[comb] += 1
                else:
                    tmp[comb] = 1
                    candidates.append(comb)

        best_comb = []
        best_comb_cnt = 2

        for comb in candidates:
            if tmp[comb] > best_comb_cnt:
                best_comb_cnt = tmp[comb]
                best_comb = [comb]
            elif tmp[comb] == best_comb_cnt:
                best_comb.append(comb)

        for best in best_comb:
            answer.append(best)

    answer.sort()
    return answer