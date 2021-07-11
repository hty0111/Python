#阶乘
a = lambda x : 1 if x == 1 else x * a(x-1)
print(a(5))

#斐波那契
a = lambda x : 1 if x==1 or x==2 else a(x-2) + a(x-1)
print(a(20))

#汉诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '->', z, end=' ')
    else:
        hanoi( n-1, x, z, y )
        print(x, '->', z, end=' ')
        hanoi( n-1, y, x, z )
hanoi( int(input()), 'X', 'Y', 'Z' )