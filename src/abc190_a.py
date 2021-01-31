A, B, C = map(int, input().split())
if A >B:
    print('Takahashi')
elif A == B:
    if C == 0:
        print('Aoki')
    else:
        print('Takahashi')
else:
    print('Aoki')