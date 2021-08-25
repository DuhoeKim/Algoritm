from collections import deque

origin_mychu = 20
mychu = 20
queue = deque([])

# 사람순서 초기화
i = 1

# 줄선횟수 담기위한 딕셔너리
cnt_person = dict()
while mychu > 0:
    # 줄 서기
    queue.append(i)

    # 신규 생성
    cnt_person[i] = 1

    input()
    # 큐에 있는 사람
    print('큐에 있는 사람 수 :', len(queue))
    print('줄 선 사람 목록 :', *queue)
    # 맨 앞사람
    p = queue.popleft()
    # 줄 선 횟수만큼 마이쮸 받기
    mychu -= cnt_person[p]
    print('맨 앞사람이 받는 마이쮸 갯수 :', cnt_person[p])

    # 마이쮸 확인
    # 음수면 0으로
    if mychu <= 0:
        mychu = 0
        print('마지막 마이쮸의 주인공 : ', p)
        break
    else:
        print('현재 맨 앞사람이 받았을 때, 나눠준 마이쮸 수 : ', origin_mychu-mychu)
        print('현재 맨 앞사람이 받았을 때, 남은 마이쮸 : ', mychu)

    # 새로 줄 세우기
    queue.append(p)
    cnt_person[p] += 1

    # 다음사람 커몬
    i += 1

