X, Y = map(int, input().split())

flag = False
for a in range(0, X+1):
    leg = 2 * a + 4 * (X-a)
    if leg == Y:
        print('Yes')
        flag = True

if not flag:
    print('No')