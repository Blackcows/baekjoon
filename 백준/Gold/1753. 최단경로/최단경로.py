import sys
input = sys.stdin.readline

import heapq
INF = float('inf')

def dijkstra(start):
    distance[start] = 0  # 시작점 초기화
    heapq.heappush(queue, (0, start))  # 시작 정점을 힙에 push

    while queue:
        dist, now = heapq.heappop(queue)  # 힙에서 최소 distance 노드를 추출

        if distance[now] < dist:  # 이전에 누적된 최소값보다 크다면 업데이트하지 않음
            continue

        for d, next_node in graph[now]:  # 다음 노드까지의 거리 누적값을 계산
            if dist + d < distance[next_node]:  # 이전에 누적된 최소값보다 작은 값이 나오면
                distance[next_node] = dist + d  # 업데이트 하고 힙에 푸쉬
                heapq.heappush(queue, (dist + d, next_node))


V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

distance = [INF for _ in range(V + 1)]
queue = []

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])
