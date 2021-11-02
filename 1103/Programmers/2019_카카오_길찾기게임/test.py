import sys
sys.setrecursionlimit(10**9)

def solution(nodeinfo):
    N = len(nodeinfo)

    new_info = list(zip(nodeinfo, [num for num in range(1, N+1)]))
    new_info.sort(key=lambda x: x[0][0])

    result1 = []
    result2 = []

    def preorder(s, e):
        if s == e:
            return
        p = new_info.index(max(new_info[s:e], key=lambda x: x[0][1]))
        # max_y = 0
        # p = 0
        # for i in range(s, e):
        #     if new_info[i][0][1] > max_y:
        #         max_y = new_info[i][0][1]
        #         p = i
        result1.append(new_info[p][1])
        preorder(s, p)
        preorder(p+1, e)
        result2.append(new_info[p][1])

    preorder(0, N)


    answer = []
    answer.append(result1)
    answer.append(result2)

    # for i, node in enumerate(nodeinfo):
    #     mat[node[1]][node[0]] = i+1
    #
    # result1 = []
    # result2 = []
    # def preorder(s, e, ys):
    #     for i in range(ys, -1, -1):
    #         flag = 0
    #         for j in range(s, e):
    #             if mat[i][j]:
    #                 result1.append(mat[i][j])
    #                 preorder(s, j, i-1)
    #                 preorder(j+1, e, i-1)
    #                 flag = 1
    #                 break
    #         if flag:
    #             break
    #
    # def postorder(s, e, ys):
    #     for i in range(ys, -1, -1):
    #         flag = 0
    #         for j in range(s, e):
    #             if mat[i][j]:
    #                 postorder(s, j, i-1)
    #                 postorder(j+1, e, i-1)
    #                 result2.append(mat[i][j])
    #                 flag = 1
    #                 break
    #         if flag:
    #             break
    # preorder(0, max_x+1, max_y)
    # postorder(0, max_x+1, max_y)
    #
    # answer = []
    #
    # answer.append(result1)
    # answer.append(result2)
    # print(answer)
    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])