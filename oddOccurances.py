def soltuion(A):
    A.sort()
    A.append(-1)
    for i in range(0, len(A), 2):
        if A[i] != A[i+1]:
            return A[i]

