def solution(S, P, Q):
    prefix_sums = [[0] * (len(S) + 1) for _ in range(4)]  # 4 rows for each nucleotide type
    for i, nucleotide in enumerate(S):
        impact_factor = {'A': 0, 'C': 1, 'G': 2, 'T': 3}[nucleotide]
        for j in range(4):
            prefix_sums[j][i + 1] = prefix_sums[j][i] + int(impact_factor == j)
    
    # Process each query
    result = []
    for i in range(len(P)):
        start_pos, end_pos = P[i], Q[i] + 1
        for nucleotide in ['A', 'C', 'G', 'T']:
            if prefix_sums[{'A': 0, 'C': 1, 'G': 2, 'T': 3}[nucleotide]][end_pos] - prefix_sums[{'A': 0, 'C': 1, 'G': 2, 'T': 3}[nucleotide]][start_pos] > 0:
                result.append({'A': 1, 'C': 2, 'G': 3, 'T': 4}[nucleotide])
                break

    return result