import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

ans = (set_a | set_b) - (set_b & set_a)
print(len(ans))