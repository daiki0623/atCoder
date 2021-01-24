N, X = map(int, input().split())
total = 0
for i in range(N):
    v, p = map(int, input().split())
    total += v * p / 100
    if total > X:
        print(i+1)
if total <= X:
    print(-1)