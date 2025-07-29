#incompleta 2 3 2

l, r, n = [int(i) for i in input().split()]

if n > r or n < l or n == 1:
    print(-1)
else:
    mult = 1
    while True:
        if mult > r:
            break
        if l <= mult <= r:
            print(mult)
        mult *= n