import itertools

N = int(input())
taste = []
smell = []
pair = set()

for i in range(N):
  A, B = map(int, input().split())
  taste.append(A)
  smell.append(B)

for comb in itertools.combinations(range(N), 2):
  i = comb[0]
  j = comb[1]
  if taste[i]*taste[j] + smell[i]*smell[j] == 0:
    pair.add(comb)

cnt = len(pair)
ans = 2**N -1 - cnt*2**(N-1)

print(ans%1000000007)
