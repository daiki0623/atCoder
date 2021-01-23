N = int(input())

branch = [0, 1]
l = []

for i in range(N):
    cond = input()
    l.append(cond)
l.reverse()

for cond in l:
    if cond == "AND":
        branch[0] += 0
        branch[1] += branch[0]
    elif cond == "OR":
        branch[0] += branch[1]
        branch[1] += branch[1]
    print(branch)

print(branch[0]+branch[1])


