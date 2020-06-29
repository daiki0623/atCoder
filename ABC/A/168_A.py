N = int(input())
hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
bon = [3]
a = N%10
if a in hon:
  print('hon')
elif a in pon:
  print('pon')
elif a in bon:
  print('bon')