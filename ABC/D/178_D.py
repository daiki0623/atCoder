S = int(input())

aS_6 = 0
aS_5 = 0
aS_4 = 1
aS_3 = 1
aS_2 = 1
aS_1 = 2
total = aS_6 + aS_5 + aS_4
for i in range(7, S+1):
    total = total - aS_6 + aS_3
    aS = total + 1
    aS_3 = aS_2
    aS_2 = aS_1
    aS_1 = aS
print(aS)


