from collections import Counter

def solution(s):
    answer = []
    cnt_num = sorted(Counter(s.replace('{', '').replace('}','').split(',')).items(), key=lambda x: x[1], reverse=True)
    for num in cnt_num:
        answer.append(int(num[0]))
    return answer