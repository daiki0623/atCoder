N, S, D = map(int, input().split())

attack = 'No'

for _ in range(N):
    x, y = map(int, input().split())
    if x < S and y > D:
        attack = 'Yes'
print(attack)
