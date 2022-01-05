import sys
sys.stdin = open("sample_input.txt")

'''
DP 풀이 : 각 달의 최소 비용을 누적해나가는 방법으로 해결
'''
T = int(input())
for test_case in range(1, T+1):
    prices = list(map(int, input().split()))                                # 가격표
    plans = [0] + list(map(int, input().split()))                           # 1년 계획 + 맨 앞 0으로 패딩

    min_price = [0]*13                                                      # 각 달까지 누적 최소 비용 + 첫달 패딩

    for month in range(1, 13):                                              # 1월 부터 12월 까지
        day_total = min_price[month-1] + plans[month] * prices[0]           # 일일권 = 전달 + 일일 가격*계획 일수
        month_total = min_price[month-1] + prices[1]                        # 한달권 = 전달 + 한달권 가격

        three_month_total = prices[3]+1                                     # 세달권 가격 초기화
        if month >= 3:                                                      # 3월이후부턴 세달권 가격 측정 가능
            three_month_total = min_price[month-3] + prices[2]              # 세달권 = 세달전 + 세달권 가격

        min_price[month] = min([day_total, month_total, three_month_total]) # 일일, 한달, 세달 중 제일 저렴한 걸로 기록

    if min_price[-1] < prices[-1]:                                          # 12월에 기록된 가격과 1년 가격 비교
        result = min_price[-1]
    else:
        result = prices[-1]

    print('#{} {}'.format(test_case, result))