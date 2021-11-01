def solution(s):
    # 문자열 초기화
    answer = 'a'*1001
    
    # 길이가 1이면 1 리턴
    if len(s) == 1:
        return 1
    
    # 1~문자열 길이의 반까지 압축 갯수를 늘려가며 검사
    for d in range(1, (len(s)//2)+1):
        # 자른 문자열을 담을 리스트 
        temp = []

        # d 만큼 잘라서 리스트에 담기
        for j in range(0, len(s), d):
            now = s[j:j+d]
            temp.append(now)
        
        cnt = 1
        ans_temp = ''
        for i in range(len(temp)-1):
            # 같은 문자 일때
            if temp[i] == temp[i+1]:
                cnt += 1

            # 다를 때
            else:
                # 연속한게 없으면 문자 그냥 누적
                if cnt == 1:
                    ans_temp += temp[i]
                # 연속한게 있으면 연속한 수 + 문자를 누적
                else:
                    ans_temp += str(cnt) + temp[i]
                cnt = 1

            # 가지치기
            if len(ans_temp) > len(answer):
                break
        # for 문 다 돌았을 때
        else:
            if cnt != 1:
                ans_temp += str(cnt) + temp[-1]
            else:
                ans_temp += temp[-1]
            
            if len(answer) > len(ans_temp):
                answer = ans_temp
    return len(answer)