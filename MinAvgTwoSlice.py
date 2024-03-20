def solution(A):
    min_avg = float('inf')
    min_pos = 0

    for i in range(len(A) - 1):
        # Calculate average of slice of length 2
        avg_2 = (A[i] + A[i + 1]) / 2
        if avg_2 < min_avg:
            min_avg = avg_2
            min_pos = i

        # Calculate average of slice of length 3
        if i < len(A) - 2:
            avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg_3 < min_avg:
                min_avg = avg_3
                min_pos = i

    return min_pos