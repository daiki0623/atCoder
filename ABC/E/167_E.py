import sys
import itertools
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
h = list(map(int, readline().split()))
A = np.array(list(itertools.combinations(range(1, N + 1), 2)))
cnt = 0
for i in range(len(A)):
    a = A[i][0]
    b = A[i][1]
    if abs(a - b) == h[a - 1] + h[b - 1]:
        cnt += 1
print(cnt)
