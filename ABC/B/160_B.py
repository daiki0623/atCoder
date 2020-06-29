X = int(input())
happy_500 = X // 500
happy_5 = (X % 500) // 5
print(1000 * happy_500 + 5 * happy_5)