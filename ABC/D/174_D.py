N = int(input())
c = input()
l = []

for i in range(len(c)):
    l.append(c[i])
cnt = l.count('R')


def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


for i in range(N):
    if l[-(i+1)] == 'R':
        if my_index(l, 'W'):
            l[l.index('W')] = 'R'
            l[-(i+1)] = 'W'
            print(i, l)
    if l.index('W') == cnt:
        print(i+1)
        break

