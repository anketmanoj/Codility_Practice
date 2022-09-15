from unittest import result


S = "ACCAABBC"
listS = list(S)
print(listS)

result = ""


for i in range(0, len(listS)):
    if S[i] == S[i+1]:
        result +=S[i]
        

print(result)