import sys
sys.stdin = open('s_input.txt')

T = int(input())
for test_case in range(1, T+1):

    N = int(input())                            # 배열 크기
    numbers = list(map(int, input().split()))   # 입력을 리스트로

    result = -1                                 # 결과 초기화

    for i in range(N-1):                        # i 의 범위 0 ~ N-2 까지
        for j in range(i+1, N):                 # j 의 범위 i 보다 크고 N-1 까지
            origin = numbers[i] * numbers[j]    # Ai * Aj 저장
            if origin < result:                 # 만약 Ai * Aj 가 현재 결과값보다 작으면
                continue                        # 다음 경우 확인
                
            check = origin                      # 두 수 곱 복사
            temp = 9                            # 마지막 자리 9로 초기화 : 9가 마지막 자리에 나올 수 있는 제일 큰 수 이기 때문에
            mode = 1                            # 단조증가인지 확인하는 토글

            while check > 0:                    # 더 이상 나눌 수 없을 때까지
                if temp >= check % 10:          # 만약 현재 마지막 자리가 이전 마지막 자리보다 작으면
                    temp = check % 10           # 현재 마지막 자리로 갱신
                else:                           # 아니라면
                    mode = 0                    # 모드 0으로. 단조증가하지 않음
                    break                       # 루프 종료

                check = check // 10             # 아직까지 단조 증가면 check 를 10으로 나누어 다음 자리 확인

            if mode and origin > result:        # 단조증가 수이고, 현재 결과보다 크면
                result = origin                 # 결과 초기화

    print('#{} {}'.format(test_case, result))



