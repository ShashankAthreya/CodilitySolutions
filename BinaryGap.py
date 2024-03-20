def solution(N):
    binary = bin(N)[2:]  # Convert N to binary representation
    max_gap = 0
    current_gap = 0
    start_counting = False
    
    for digit in binary:
        if digit == '1':
            if not start_counting:
                start_counting = True
            else:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
        elif start_counting:
            current_gap += 1
    
    return max_gap