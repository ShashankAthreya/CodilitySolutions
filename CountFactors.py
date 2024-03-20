import math

def solution(N):
    factors = 0
    sqrt_N = int(math.sqrt(N))
    
    for i in range(1, sqrt_N + 1):
        if N % i == 0:
            factors += 2
    
    if sqrt_N * sqrt_N == N:
        factors -= 1
        
    return factors
