E = "23:58"
L = "23:59"

entryHour = E.split(":")[0]
entryMin = E.split(":")[1]

exitHour = L.split(":")[0]
exitMin = L.split(":")[1]

timeInHours = int(exitHour) - int(entryHour)
timeInPer = (int(exitMin) / 60) - (int(entryMin) / 60)
timeInMin = int(60 * timeInPer)



cost = 2

if timeInHours > 1 and timeInMin >= 0:
    cost +=4

if timeInHours >= 1 or timeInMin >= 0:
    cost += 3

for i in range(1, timeInHours):
    cost += 4

# if timeInHours >= 1 or timeInMin > 0:
#     cost += 4
    

print(f"cost == {cost}")
