N, M = map(int, input().split())
A = list(map(int, input().split()))
homework = sum(A)
playday = N - homework
if playday >= 0:
  print(playday)
else:
  print(-1)