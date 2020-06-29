L = int(input())
Lfloat = L * 100
MAX = 0
for a in range(int(Lfloat/3)+1):
  for b in range(Lfloat-a+1):
    val = a/100 * b/100 * (Lfloat - a- b)/100
    if val > MAX:
      MAX = val
print(MAX)