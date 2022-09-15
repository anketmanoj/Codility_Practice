N = 24
maxK = 21
lastVal = 0

for i in range(maxK):
    if N % 2**i == 0:
        lastVal = i

print(lastVal)


