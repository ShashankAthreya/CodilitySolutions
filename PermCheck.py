def solution(A):
    n = len(A)
    total = (n+1) * (n) // 2
    if total - sum(list(set(A))) == 0: return 1
    return 0