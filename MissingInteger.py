def solution(A):
    A = sorted(set(A))
    if max(A) < 1: return 1
    A = [x for x in A if x > 0]
    if A[0] != 1: return 1
    i = 1
    for i in range(len(A)):
        if A[i-1] + 1 < A[i]: return (A[i-1] + 1)
    return (A[i]+1)