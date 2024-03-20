def solution(A):
    N = len(A)
    
    left = [0] * N
    right = [0] * N

    for i in range(N):
        left[i] = i - A[i]
        right[i] = i + A[i]

    left.sort()
    right.sort()

    intersections = 0
    j = 0

    for i in range(N):
        while j < N and right[i] >= left[j]:
            j += 1
        intersections += j - i - 1

        if intersections > 10000000:
            return -1
    
    return intersections