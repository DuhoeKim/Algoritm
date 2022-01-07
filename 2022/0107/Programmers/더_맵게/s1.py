import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        m = heapq.heappop(scoville)
        if m >= K:
            return answer
        if not len(scoville):
            return -1
        mm = heapq.heappop(scoville)

        new_food = m + (mm * 2)
        answer += 1
        heapq.heappush(scoville, new_food)
