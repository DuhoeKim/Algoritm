def merge(u, v):
    result = ''
    if not v:
        if u[0] == ')' or u[-1] == '(':
            result += '()'
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    result += ')'
                else:
                    result += '('
            return result
        else:
            return u
    mu, mv = separate(v)
    if u[0] == ')' or u[-1] == '(':
        result += '('
        result += merge(mu, mv)
        result += ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                result += ')'
            else:
                result += '('
    else:
        result += u
        result += merge(mu, mv)

    return result

def separate(s):
    u, v = '', ''
    idx = {
        ')': 0,
        '(': 1,
        }
    cnt = [0, 0]
    flag = False
    for i in s:
        if flag:
            v += i
            continue

        u += i
        cnt[idx[i]] += 1
        if cnt[0] == cnt[1]:
            flag = True

    return (u, v)

def solution(p):
    answer = ''
    u, v = separate(p)
    answer = merge(u, v)
    return answer

print(solution(')('))
print(solution("(()())()"))
print(solution("()))((()"))