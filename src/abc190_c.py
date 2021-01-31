N, M = map(int, input().split())
cond = []
for _ in range(M):
    cond.append(list(map(int, input().split())))
K = int(input())
cases = []
for _ in range(K):
    cases.append(list(map(int, input().split())))

maximumCnt = 0
for i in range(2 ** K):
    case = list(map(int, format(i, 'b').zfill(K)))
    ballsOnDish = set()
    for j in range(K):
        ballsOnDish.add(cases[j][case[j]])
    cnt = 0
    for j in range(M):
      if cond[j][0] in ballsOnDish and cond[j][1] in ballsOnDish:
        cnt += 1

    if cnt > maximumCnt:
        maximumCnt = cnt
print(maximumCnt)
