N, M, Q = map(int, input().split())
import itertools
comb = itertools.combinations_with_replacement(range(1, M+1), N)
MAX = 0

val = []
for i in range(Q):
  val.append(list(map(int, input().split())))

for l in comb:
  ans = 0
  for i in range(Q):
    a, b, c, d = val[i][0], val[i][1], val[i][2], val[i][3]
    if l[b-1] - l[a-1] == c:
      ans += d
  if ans > MAX:
    MAX = ans
print(MAX)