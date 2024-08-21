import sys
input = sys.stdin.readline

n = int(input())

x, y, z = 0, 1, 1
mod = 1000000007

for _ in range(n-2):
    x = y % mod
    y = z % mod
    z = (x % mod + y % mod) % mod

print(z, n-2)
