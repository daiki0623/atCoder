X, N = map(int, input().split())
if N == 0:
    print(X)
    exit(0)
l = list(map(int, input().split()))

n = 0
while True:
    candidate = X - n
    if candidate not in l:
        print(candidate)
        break
    candidate = X + n
    if candidate not in l:
        print(candidate)
        break
    n += 1