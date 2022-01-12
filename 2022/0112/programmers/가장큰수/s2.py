def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: int(str(x)[0]) % 10, reverse=True)
    

    return answer