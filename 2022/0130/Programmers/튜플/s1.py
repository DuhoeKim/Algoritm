def solution(s):
    answer = []
    s = s.split('},{')
    for i in range(len(s)):
        s[i] = s[i].replace('{', '')
        s[i] = s[i].replace('}', '')
        s[i] = s[i].split(',')
        s[i] = list(map(int, s[i]))
    s.sort(key=lambda x: len(x))
    visited = [0] * 100001
    for lst in s:
        for num in lst:
            if visited[num]:
                continue
            visited[num] = 1
            answer.append(num)
    return answer