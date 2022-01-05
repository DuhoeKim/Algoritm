def solution(new_id):
    N = len(new_id)
    allowed = ['-', '_', '.']
    # 1단계
    new_id = new_id.lower()
   

    # 2단계
    temp = ''
    for s in new_id:
        if (s in allowed) or (s.isdigit()) or (s.isalpha()):
            temp += s

    # 3단계
    tmp = temp
    temp = ''
    flag = 0
    for s in tmp:
        if s == '.':
            if flag == 0:
                temp += s
                flag = 1
        else:
            flag = 0
            temp += s

            
    # 4단계
    temp = temp.strip('.')

    # 5단계
    if not temp:
        temp += 'a'

    # 6단계
    temp = temp[:15].strip('.')

    # 7단계
    while len(temp) <=2 :
        temp += temp[-1]
    answer = temp

    return answer