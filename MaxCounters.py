def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_max = 0

    for operation in A:
        if 1 <= operation <= N:
            counters[operation - 1] = max(counters[operation - 1], max_counter) + 1
            current_max = max(current_max, counters[operation - 1])
        elif operation == N + 1:
            max_counter = current_max

    for i in range(N):
        counters[i] = max(counters[i], max_counter)

    return counters