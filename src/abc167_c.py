import itertools
N, M, X= map(int, input().split())

p = []
u = []

for i in range(N):
  t = list(map(int, input().split()))
  p.append(t[0])
  u.append(t[1:])

candidate = []
for i in range(1, N+1): #ここがM+1になってた
  for comb in itertools.combinations(range(N), i):
    price = 0
    understand = [0]*M
    for j in range(i):
      price += p[comb[j]]
      understand = [x + y for (x, y) in zip(understand, u[comb[j]])]
    if all(elem >= X for elem in understand):
      candidate.append(price)

if candidate == []:
  print(-1)
else:
  print(min(candidate))