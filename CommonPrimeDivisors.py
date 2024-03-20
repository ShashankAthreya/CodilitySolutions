def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def has_same_prime_divisors(a, b):
    gcd_value = gcd(a, b)
    while a != 1:
        gcd_a = gcd(a, gcd_value)
        if gcd_a == 1:
            break
        a //= gcd_a
    if a != 1:
        return False
    while b != 1:
        gcd_b = gcd(b, gcd_value)
        if gcd_b == 1:
            break
        b //= gcd_b
    return b == 1

def solution(A, B):
    count = 0
    for a, b in zip(A, B):
        if a==b or has_same_prime_divisors(a, b):
            count += 1
    return count
