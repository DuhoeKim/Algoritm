def is_palindrome(s):
    n = len(s)
    if n % 2:
        return False
    if s[:n//2] == s[n//2:][::-1]:
        return True
    else:
        return False
def solution(s):
    answer = 1
    for i in range(97, 123):
        if s.count(chr(i)) % 2:
            answer = 0
            return answer

    alphs = list(set(s))
    before_s = s
    while s:
        if is_palindrome(s):
            break

        for alph in alphs:
            s = s.replace(alph*2, '')

        if before_s == s:
            answer = 0
            break
        before_s = s

    return answer

print(solution('bcbaab'))