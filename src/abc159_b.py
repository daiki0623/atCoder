S = input()
N = len(S)
S1 = S[:int((N-1)/2)]
S2 = S[int((N+1)/2) : N]
l = [S, S1, S2]
ans = 'Yes'

for s in l:
  for i in range(len(s)):
    a = s[i]
    b = s[-(i+1)]
    if a != b:
      ans = 'No'

print(ans)

