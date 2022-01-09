def find(v):
    global check
    if check[v] == v:
        return v
    return find(check[v])

def union(r1, r2):
    global check
    check[r2] = r1
    for i in range(len(check)):
        if check[i] == r2:
            check[i] = r1

def solution(n, costs):
    global check
    answer = 0
    costs.sort(key=lambda x: x[2])
    check = [i for i in range(n)]
    done = 0
    for v1, v2, cost in costs:
        r1 = find(v1)
        r2 = find(v2)
        if r1 != r2:
            union(r1, r2)
            done += 1
            answer += cost
        if done == n - 1:
            break
    return answer