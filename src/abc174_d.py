N = int(input())
c = input()

numR = c.count('R')
print(0 if numR == 0 or numR == len(c) else c[:numR].count('W'))
