def gys(a, b, c = 0):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def solution(w, h):
    answer = 0
    origin = w * h
    G = gys(w, h)
    w //= G
    h //= G
    answer = origin - G * (w + h - 1)
    return answer