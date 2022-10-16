t = int(input())

for i in range(t):
    n = int(input())
    l, r = 0, 1
    while n > 0:
        temp = r
        r += l
        l = temp
        n -= 1
    print(r)