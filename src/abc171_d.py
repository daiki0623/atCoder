from collections import Counter
N = int(input())
A = list(map(int, input().split()))
S = sum(A)
Q = int(input())

dict = Counter(A)
for i in range(Q):
    l = list(map(int, input().split()))
    d = l[1] - l[0]
    cnt = dict[l[0]]
    dict[l[1]] += dict[l[0]]
    dict.pop(l[0], None)
    S += d*cnt
    print(S)