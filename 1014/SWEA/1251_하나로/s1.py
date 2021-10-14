import sys
sys.stdin = open("input.txt")

# 모든 다리의 길이를 구하는 함수
def get_bridges():
    # 2가지 선택 n C 2
    for i in range(N-1):
        for j in range(i+1, N):
            # 피타고라스 정리 활용
            L = (abs(island[i][0]-island[j][0]) ** 2 + abs(island[i][1] - island[j][1]) ** 2) ** 0.5
            bridges.append([i, j, L])   # 연결된 두 섬의 번호와 다리 길이를 bridges 에 추가

def find_set(x):
    if sets[x] == x:
        return x
    return find_set(sets[x])

def union(n1, n2):
    r1 = find_set(n1)
    r2 = find_set(n2)
    sets[r2] = r1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    island = [[0]*2 for _ in range(N)]
    
    # 섬 좌표 정보 입력
    for i in range(2):
        info = list(map(int, input().split()))
        for j in range(N):
            island[j][i] = info[j]
    
    # 세율
    E = float(input())
    
    # 서로소 생성
    sets = [num for num in range(N)]

    # 모든 다리 길이 구하기
    bridges = []                        # 다리 길이 정보 초기화
    get_bridges()
    bridges.sort(key=lambda x: x[2])    # KRUSKAL 을 위해 소팅

    L = 0                               # L 값 초기화
    connected = 0                       # 연결된 다리 수 초기화


    # KRUSKAL
    for bridge in bridges:
        n1, n2, l = bridge
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            L += l*l
            connected += 1
            if connected == N-1:
                break

    # 결과구하기 ( 첫째자리 반올림 )
    result = round(E * L)

    print('#{} {}'.format(test_case, result))