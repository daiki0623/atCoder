N = int(input())

item = list(map(int, input().split()))

max_orange = 0
for i in range(len(item)):
    val = item[i]
    cnt = 1
    for j in range(1, i+1):
        try:
            if val <= item[i-j]:
                cnt += 1
            else:
                break
        except:
            break
    for j in range(1, N-i):
        try:
            if val <= item[i+j]:
                cnt += 1
            else:
                break
        except:
            break
    candidate = val * cnt
    if candidate > max_orange:
        max_orange = candidate

print(max_orange)

