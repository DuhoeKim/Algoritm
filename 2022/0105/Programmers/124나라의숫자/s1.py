def solution(n):
    answer = ''
    code = n % 3
    if code == 0:
        answer += '4'
        n -= 3
    else:
        answer += str(n % 3)
        n -= n % 3
    while n:
        flag = 0
        if (n // 3) >= 4:
            code = str((n//3)%3)
        elif (n // 3) == 3:
            code = '4'
        else:
             code = n // 3

        if code == 0:
            break
        elif code == '0':
            code = '4'
            flag = 1
        if (n // 3) == 3:
            answer = str(code) + answer
            break
        answer = str(code) + answer
        n = n // 3
        if flag:
            n -= 3
    return answer