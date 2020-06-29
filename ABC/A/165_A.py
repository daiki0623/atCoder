K = int(input())
A, B = map(int, input().split())

l = [i for i in range(A, B+1)]

for i in l:
  if i%K == 0:
    print('OK')
    break
  if i == l[-1] and i%K != 0:
    print('NG')