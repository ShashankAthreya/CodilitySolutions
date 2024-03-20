def solution(A):
    count_zeros = 0
    passing_cars = 0

    for car in A:
        if car == 0:
            count_zeros += 1
        else:
            passing_cars += count_zeros
            if passing_cars > 1000000000:
                return -1

    return passing_cars