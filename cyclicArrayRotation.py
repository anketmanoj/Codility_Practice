
def solution(A, K):
    old = A
    new = [0]*len(A)
    print(f"new == {new}")
    for i in range(K):
        new[0] = old[-1]
        new[1:]=old[:-1]
        old = new.copy()
    print(old)
    return new

solution([1,2,3,4,5], 2)