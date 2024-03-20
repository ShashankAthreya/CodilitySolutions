def solution(X, Y, D):
    # return int((X+Y)/D)
    dist = Y - X
    if dist == 0: return 0
    if dist % D == 0:
        return int(dist/D)
    return (int(dist/D)+1)
