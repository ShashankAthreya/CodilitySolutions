def solution(A, B):
    total_fish = len(A)
    if 1 not in B or 0 not in B: return total_fish

    down_fish = []
    alive_fish = 0

    for i in range(total_fish):
        if B[i] == 1:
            down_fish.append(A[i])
        else:
            while down_fish:
                if A[i] > down_fish[-1]:
                    down_fish.pop()
                else:
                    break
            else:
                alive_fish += 1
    
    alive_fish += len(down_fish)
    
    return alive_fish
