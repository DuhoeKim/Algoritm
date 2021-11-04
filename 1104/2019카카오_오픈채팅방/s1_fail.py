def solution(records):
    answer = []
    logs = []

    for record in records:
        info = record.split(' ')

        # 입장일 때,
        if info[0] == 'Enter':
            # 로그 확인.
            for log in logs:
                # 들어왔던 적이 있는 사람이면,
                if log['uid'] == info[1]:
                    # 닉네임 변경
                    log['nick_name'] = info[2]
                    # 메세지 인덱스 기록 후 메세지 추가
                    answer.append("님이 들어왔습니다.")
                    log['msg_idx'].append(len(answer) - 1)
                    # 로그 확인 중단
                    break
            # 들어온적 없으면,
            else:
                answer.append("님이 들어왔습니다.")
                logs.append({
                    'uid': info[1],
                    'nick_name': info[2],
                    'msg_idx': [len(answer) - 1],
                })


        elif info[0] == 'Leave':
            for log in logs:
                if log['uid'] == info[1]:
                    answer.append("님이 나갔습니다.")
                    log['msg_idx'].append(len(answer) - 1)
                    break

        else:
            for log in logs:
                if log['uid'] == info[1]:
                    log['nick_name'] = info[2]
                    break

    for log in logs:
        for idx in log['msg_idx']:
            answer[idx] = log['nick_name'] + answer[idx]

    return answer