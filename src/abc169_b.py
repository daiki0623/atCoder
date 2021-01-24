N = int(input())
l = list(map(int, input().split()))

ans = 1
for i in l:
    ans *= i
    if ans > 10 ** 18:
        break

if ans > 10 ** 18:
    print('-1')
else:
    print(ans)