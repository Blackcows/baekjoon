import sys
input = sys.stdin.readline

import heapq

n = int(input())
queue = []

for i in range(n):
    num = int(input())

    if num == 0:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
    else:
        heapq.heappush(queue, (abs(num), num))
