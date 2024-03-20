def fib_up_to(n):
    numbers = [1]
    i = 1
    while True:
        new_num = (numbers[-2] + numbers[-1]) if i > 1 else 2
        if new_num > n:
            break
        numbers.append(new_num)
        i += 1
    return numbers

def solution(A):
    n = len(A)
    if n == 0:
        return 1
    numbers = fib_up_to(n+1)

    possible_positions = set([-1])
    for k in range(1, n+1):
        positions_after_k = set()
        for pos in possible_positions:
            for jump in numbers:
                if pos + jump == n:
                    return k
                if pos + jump < n and A[pos + jump]:
                    positions_after_k.add(pos + jump)
        possible_positions = positions_after_k
    return -1
