# Compute number of integers divisible by k in range [a..b].

def solution(A, B, K):
    b = B // K
    a = (A-1) // K if A > 0 else 0
    if A == 0 or B == 0: return (b-a+1)

    return (b-a)