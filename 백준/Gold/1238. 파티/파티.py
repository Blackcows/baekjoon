import sys
input = sys.stdin.readline

import heapq
INF = float('inf')

def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0  # 시작점 초기화
    queue = []
    heapq.heappush(queue, (0, start))  # 시작 정점을 힙에 push

    while queue:
        dist, now = heapq.heappop(queue)  # 힙에서 최소 distance 노드를 추출

        if distance[now] < dist:  # 이전에 누적된 최소값보다 크다면 업데이트하지 않음
            continue

        for d, next_node in graph[now]:  # 다음 노드까지의 거리 누적값을 계산
            if dist + d < distance[next_node]:  # 이전에 누적된 최소값보다 작은 값이 나오면
                distance[next_node] = dist + d  # 업데이트 하고 힙에 푸쉬
                heapq.heappush(queue, (dist + d, next_node))

    return distance


# 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
# 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append([t, v])

ans = dijkstra(X)  # 1) 단방향 그래프에서 X 지점으로부터 각 마을까지의 거리
ans[0] = 0
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)  # 2) 단방향 그래프에서 각 마을로부터 X지점 까지의 최단거리
        ans[i] += res[X]   # 둘을 누적

print(max(ans))
