def solution(phone_book):
    answer = True
    check = dict()
    for number in phone_book:
        check[number] = 1
    for number in phone_book:
        tmp = ''
        for n in number:
            tmp += n
            if check.get(tmp) and tmp != number:
                return False
    return answer