N = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
cnt = 0
for a in l[1:]:
    if l[0] % a == 0:
        break
    if a == l[-1]:
        cnt += 1

for i in range(1, len(l)-1):
    if l[i] != l[i+1] and l[i] != l[i-1]:
        for j in reversed(range(i+1, len(l))):
            if l[i] % l[j] == 0:
                break
            if j == i+1:
                cnt += 1

if l[-1] == l[-2]:
    print(cnt)
else:
    print(cnt+1)