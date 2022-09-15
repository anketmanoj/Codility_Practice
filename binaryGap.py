def solution(N):
    N = bin(N)[2:]
    print(N)
    b=0
    maxB=0
    for k in N:
        if int(k)==0:
            b+=1
        elif int(k)==1:
            maxB=max(b, maxB)
            b=0
    return maxB

print(solution(837837))