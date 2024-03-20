def solution(A):
    A.sort()
    n = len(A) - 1
    return(max(A[n] * A[n-1] * A[n-2], A[0] * A[1] * A[n]))