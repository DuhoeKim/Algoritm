def solution(str1, str2):

    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    comb = 0
    inter = 0

    record = dict()

    for i in range(len(str1)-1):
        tmp = str1[i] + str1[i+1]
        if tmp.isalpha():
            comb += 1
            record[tmp] = 1 if not record.get(tmp) else record[tmp] + 1

    for i in range(len(str2)-1):
        tmp = str2[i] + str2[i+1]
        if tmp.isalpha():
            if record.get(tmp):
                record[tmp] -= 1
                inter += 1
            else:
                comb += 1

    if not comb:
        return 65536
    else:
        answer = inter/comb

    return int(answer*65536)