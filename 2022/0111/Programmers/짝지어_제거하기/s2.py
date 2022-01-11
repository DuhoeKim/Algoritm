def solution(s):
    answer = []

    for i in range(97, 123):
        if s.count(chr(i)) % 2:
            answer = 0
            return answer

    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)
    if answer:
        return 0
    return 1