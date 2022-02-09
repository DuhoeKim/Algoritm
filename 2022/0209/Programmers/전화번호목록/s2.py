def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    check = dict()
    for number in phone_book:
        tmp = ''
        for n in number:
            tmp += n
            if check.get(tmp):
                return False
        check[number] = 1
    return answer