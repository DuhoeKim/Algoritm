def solution(records):
    answer = []
    nick_match = dict()

    for record in records:
        temp = record.split(' ')
        if len(temp) == 3:
            nick_match[temp[1]] = temp[2]

    for record in records:
        temp = record.split(' ')

        if temp[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(nick_match[temp[1]]))
        elif temp[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(nick_match[temp[1]]))

    return answer