from itertools import permutations
def solution(numbers):
    answer = '0'
    for p in permutations(numbers, len(numbers)):
        if int(str(p[0])[0]) < int(answer[0]):
            continue
        p = list(map(str, p))
        tmp = ''.join(p)
        answer = str(max(int(answer), int(tmp)))
    return answer