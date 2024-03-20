def find_leader(A):
    stack = []

    for num in A:
        if stack and stack[-1] != num:
            stack.pop()
        else:
            stack.append(num)
    
    if not stack:
        return -1
    
    candidate = stack[-1]
    count = A.count(candidate)
    
    if count > len(A) // 2:
        return candidate
    else:
        return -1

def solution(A):
    leader = find_leader(A)
    
    if leader == -1:
        return 0
    
    leader_count = A.count(leader)
    equi_leaders = 0
    prefix_count = 0
    suffix_count = leader_count
    
    for i in range(len(A)):
        if A[i] == leader:
            prefix_count += 1
            suffix_count -= 1
        
        if prefix_count > (i + 1) // 2 and suffix_count > (len(A) - i - 1) // 2:
            equi_leaders += 1
    
    return equi_leaders
