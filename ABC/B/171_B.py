N, K = map(int, input().split())

l = list(map(int, input().split()))
l.sort()
total = 0
for i in range(K):
    total += l[i]
print(total)
