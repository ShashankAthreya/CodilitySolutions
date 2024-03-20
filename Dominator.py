from collections import Counter 
def solution(A):
    if not A: return -1
    n = len(A)
    if n < 2: return 0
    data = Counter(A)
    max_occurences = max(list(data.values()))
    if max_occurences <= (n//2): return -1
    mode = [x for x in data if data[x] == max_occurences][0]
    return A.index(mode)