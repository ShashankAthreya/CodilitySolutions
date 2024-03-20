def solution(S):
    n = len(S)
    if n == 0: return 1
    if n % 2 != 0: return 0
    if n//2 != S.count(S[0]): return 0
    if S[0] == ')': return 0
    stack = []

    for s in S:
        if s == '(': 
            stack.append(s)
            continue
        if not stack and s == ')':
            return 0
        else:
            if stack[-1] != '(': return 0
            stack.pop()
        
    return 1 if not stack else 0