import sys
input = sys.stdin.readline

n = int(input())
mod = 10 ** 6
# mod = 10**n이면, p = 15*10**(n-1)
p = 15 * 10**5

n %= p
x, y = 0, 1
for _ in range(n):
    x, y = y % mod, (x+y) % mod

print(x)
