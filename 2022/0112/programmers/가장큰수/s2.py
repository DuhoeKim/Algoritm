# def solution(numbers):
#     if not sum(numbers):
#         return '0'
#     numbers.sort(key=lambda x: (int(str(x)[0]) % 10, int(str(x)[1 if len(str(x)) >= 2 else 0]) % 10, int(str(x)[2 if len(str(x)) >= 3 else 0]) % 10, int(str(x)[3 if len(str(x)) >= 4 else 0]) % 10), reverse=True)
#     print(numbers)
#     answer = ''.join(map(str, numbers))
#     return answer
def s2(numbers):
    if not sum(numbers):
        return '0'
    numbers.sort(key=lambda x: int((str(x)*4)[:4]), reverse=True)
    print(numbers)
    answer = ''.join(map(str, numbers))
    return answer
arr = [90, 901, 9097]
# a = int(solution(arr))
b = int(s2(arr))

# print(a-b, b-a)