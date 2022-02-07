def calc(expression, marks):
    temp = ''
    stack = []
    postfix = []

    for s in expression:
        if s.isdigit():
            temp += s
        else:
            postfix.append(int(temp))
            temp = ''
            while stack and marks.index(s) <= marks.index(stack[-1]):
                last_stack = stack.pop()
                postfix.append(last_stack)
            stack.append(s)

    postfix.append(int(temp))
    while stack:
        postfix.append(stack.pop())

    for s in postfix:
        if isinstance(s, int):
            stack.append(s)
        else:
            s2 = stack.pop()
            s1 = stack.pop()
            if s == '*':
                tmp = s1 * s2
            elif s == '-':
                tmp = s1 - s2
            else:
                tmp = s1 + s2
            stack.append(tmp)

    return stack[-1]

def solution(expression):
    answer = 0
    candidates = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '-', '+'],
        ['*', '+', '-'],
    ]

    for candidate in candidates:
        answer = max(answer, abs(calc(expression, candidate)))
    return answer