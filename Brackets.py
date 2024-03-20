def solution(S):
    if not S: return 1
    s = list(S)
    n = len(s)
    if n % 2 != 0: return 0
    stack = []

    for b in s:
        if b == '{' or b == '[' or b == '(':
            stack.append(b)
        if b == '}':
            if not stack: return 0
            temp = stack.pop()
            if temp != '{': 
                return 0
        if b == ']':
            if not stack: return 0
            temp = stack.pop()
            if temp != '[': 
                return 0
        if b == ')':
            if not stack: return 0
            temp = stack.pop()
            if temp != '(': 
                return 0
    
    if stack: return 0

    return 1
