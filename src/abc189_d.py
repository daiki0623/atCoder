N = int(input())

branch = [0, 1]
l = []

for i in range(N):
    cond = input()
    l.append(cond)
l.reverse()

for cond in l:
    val0, val1 = branch[0], branch[1]
    if cond == "AND":
        branch[0] += val0
        branch[1] += val0
    elif cond == "OR":
        branch[0] += val1
        branch[1] += val1
print(branch[0]+branch[1])


