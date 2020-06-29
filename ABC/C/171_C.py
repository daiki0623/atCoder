N = int(input())

cnt = 0
n = 0
while n >= 0:
    if N > cnt:
        n += 1
        cnt += 26**n
    else:
        break
aToz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = N - (cnt - 26**n) - 1
ans = ""
for i in range(n):
    str = aToz[number % 26]
    ans += str
    number = number // 26
print(ans[::-1])