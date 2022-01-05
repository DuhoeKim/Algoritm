import sys
sys.stdin = open("sample_input.txt")

def isInRange(y, x):
    if 0 <= x < 4 and 0 <= y < 4:
        return True
    return False

def DFS(r, c, w):
    w += mat[r][c]
    if len(w) == 7:
        if w not in wordlist:
            wordlist.append(w)
        return
    dx = [0 , 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]

        if isInRange(nr, nc):
            DFS(nr, nc, w)

T = int(input())

for test_case in range(1, T+1):

    mat = [input().split() for _ in range(4)]

    wordlist = []

    for i in range(4):
        for j in range(4):
            word = ''
            DFS(i, j, word)

    result = len(wordlist)

    print('#{} {}'.format(test_case, result))