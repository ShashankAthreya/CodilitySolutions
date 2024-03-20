def solution(A, K):
    n = len(A)
    if n == 0 or K == 0 or not A: return A
    k = K % n

    return(A[n-k:] + A[:n-k])