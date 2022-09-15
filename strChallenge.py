def solution(S):
    reverse  = S[:len(S)//2:-1]
    straight = S[:len(S)//2]
    count = 0
    for i in range(len(straight)):
        if straight[i] != reverse[i]:
            count = 0
            
        else:
            count+=1
    
    # print(count)
    return count
    pass

solution("anket")