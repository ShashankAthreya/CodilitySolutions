# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

def solution(A):
    if not A: return 0
    n = len(A)
    if n == 1: return A[0]
    if n == 2: return abs(A[0] - A[1])
    
    left = []
    right = []

    add = 0

    for i in range(n-1):
        add += A[i]
        left.append(add)
    
    add += A[n-1] 

    for i in range(n-1):
        add -= A[i]
        right.append(add)

    # print(left,right)
    add = float('Inf')
    for i in range(n-1):
        add = min(add, abs(left[i] - right[i]))
    
    return add