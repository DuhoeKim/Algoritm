def DFS(arr, target, result, step=0, sum=0):
    if step == len(arr):
        if sum == target:
            result += 1
        return result
    result = DFS(arr, target, result, step+1, sum + arr[step])
    result = DFS(arr, target, result, step+1, sum - arr[step])
    return result

def solution(numbers, target):
    answer = 0

    answer = DFS(numbers, target, answer)
    return answer

print(solution([1,1,1,1,1], 3))