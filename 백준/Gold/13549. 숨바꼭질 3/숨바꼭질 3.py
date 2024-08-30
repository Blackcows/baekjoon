import sys
input = sys.stdin.readline

import heapq
INF = float('inf')


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for n in (now + 1, now - 1, now * 2):
            if n < 0 or n > 100000:  # 문제에서 요구한 범위를 넘어가면 처리하지 않음
                continue

            cost = dist
            if n != now * 2:  # 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
                cost = dist + 1  # 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.

            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(queue, (cost, n))


N, K = map(int, input().split())

distance = [INF for _ in range(100001)]
queue = []

dijkstra(N)
print(distance[K])
