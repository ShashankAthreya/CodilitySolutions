# Find the earliest time when a frog can jump to the other side of a river.

def solution(X, A):
    present = set()
    for i in range(len(A)):
        present.add(A[i])
        if len(present) == X:
            return i
    return -1