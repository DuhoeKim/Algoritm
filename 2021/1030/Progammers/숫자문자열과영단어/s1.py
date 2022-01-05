def solution(s):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(10):
        s = s.replace(eng[i], f'{i}')
    answer = int(s)
    return answer