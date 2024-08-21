import sys
input = sys.stdin.readline

n = int(input())

import heapq
queue = []

for _ in range(n):
    heapq.heappush(queue, int(input()))

ans = 0

while len(queue) > 1:
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)

    temp = a+b
    ans += temp
    heapq.heappush(queue, temp)

print(ans)
