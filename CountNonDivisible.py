def solution(A):
    max_num = max(A)
    counts = [0] * (max_num + 1)
    for num in A:
        counts[num] += 1

    divisors = [0] * (max_num + 1)
    for num in range(1, max_num + 1):
        for multiple in range(num, max_num + 1, num):
            divisors[multiple] += counts[num]

    result = []
    for num in A:
        non_divisors = len(A) - divisors[num]
        result.append(non_divisors)

    return result
