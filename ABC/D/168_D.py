N, K = map(int, input().split())
A = list(map(int, input().split()))

visited = []
next = 1

for i in range(1, K+1):
  present = next
  if i == K:
    print(present)
    exit(0)

  visited.append(present)
  next = A[present-1]
  if next in visited:
    ind = visited.index(next)
    l = len(visited[ind:])
    cnt = i
    break

rest = (K-cnt) % l
if rest == 0:
  print(present)
else:
  present = visited[ind + rest]
  print(present)
