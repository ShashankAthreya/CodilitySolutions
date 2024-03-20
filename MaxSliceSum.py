def solution(A):
    max_sum = A[0]
    max_so_far = A[0]

    for a in A[1:]:
        max_so_far = max(a, max_so_far + a)
        max_sum = max(max_sum, max_so_far)
    
    return max_sum
