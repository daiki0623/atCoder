N, X = map(int, input().split())
total = 0
ans = -1
for i in range(N):
    v, p = map(int, input().split())
    total += v * p
    if total > X * 100:
        ans = i + 1
        break
print(ans)
