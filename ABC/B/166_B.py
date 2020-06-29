N, K = map(int, input().split())
l = []
for i in range(K):
  d = int(input())
  A = map(int, input().split())
  for j in A:
    l.append(j)
l = set(l)
print(N - len(l))