N, M = map(int, input().split())
H = list(map(int, input().split()))

l = H.copy()
for i in range(M):
    A, B = map(int, input().split())
    if H[A - 1] > H[B - 1]:
        l[B - 1] = 0
    elif H[B - 1] > H[A - 1]:
        l[A - 1] = 0
    elif H[A - 1] == H[B - 1]:
        l[A - 1] = 0
        l[B - 1] = 0
print(N - l.count(0))
