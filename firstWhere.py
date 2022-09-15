def solution(A):
    counts = {}

    for i in A:
        if i in counts:
            counts[i] += 1
            
        else:
            counts[i] = 1

    for i in A:
        if counts[i] == 1:
            print(counts)
            print(i)
            return i
    
    print(counts)
    return -1

solution([1,4,3,3,1,2])