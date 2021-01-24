N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [-1] * N
visited[0] = 0
next = A[0]
for i in range(1, K+1):
    present = next
    visited[present - 1] = i

    next = A[present - 1]
    if visited[next - 1] != -1:
        loopLength = visited[present - 1] - visited[next - 1] + 1
        rest = (K - i) % loopLength
        if rest > 0:
            present = visited.index(visited[next - 1] + rest - 1) + 1
        break

print(present)
