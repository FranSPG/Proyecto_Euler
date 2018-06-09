import sys
sys.setrecursionlimit(1500)

def sum_mult_3_and_5(n):
    if(n == 0): return 0
    if ((n % 3 == 0) or (n % 5 == 0)):
        return (sum_mult_3_and_5(n-1) + n)
    else:
        return (sum_mult_3_and_5(n-1))

a = sum_mult_3_and_5(999)
print(a)

