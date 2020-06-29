X = int(input())

cash = 100
year = 0
while cash < X:
  cash = int(cash * 1.01)
  year += 1
print(year)