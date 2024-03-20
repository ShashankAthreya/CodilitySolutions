def solution(A):
    if not A: return 0
    minimum = float('Inf')
    profit = 0

    for a in A:
        minimum = min(minimum, a)
        profit = max(a-minimum, profit)
    
    return profit
