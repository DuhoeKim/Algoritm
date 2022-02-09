def solution(phone_book):
    answer = True
    N = len(phone_book)
    phone_book.sort(key=lambda x: len(x))
    for i in range(N-1):
        check_number = phone_book[i]
        for j in range(i+1, N):
            targer_number = phone_book[j]
            if not targer_number.split(check_number)[0]:
                return False

    return answer