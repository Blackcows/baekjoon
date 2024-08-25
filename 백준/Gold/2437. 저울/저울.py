import sys
input = sys.stdin.readline
import heapq

n = int(input())
weight = list(map(int, input().split()))
weight.sort()

total = 1
for idx in weight:
    if total < idx:
        break
    total += idx

print(total)