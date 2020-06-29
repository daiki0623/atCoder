K, N = map(int, input().split())
A = list(map(int, input().split()))
d = []
interval = 0
for i in range(1, N):
  d.append(A[i] - A[i-1])
d.append(K-A[N-1]+A[0])
print(K - max(d))