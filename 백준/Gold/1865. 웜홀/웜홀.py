import sys
input = sys.stdin.readline


def bellman_ford():
    # N번 검사
    for i in range(N):
        # 모든 루트에 대해
        for r in route:
            start, goal, time = r
            if distance[goal] > distance[start] + time:
                distance[goal] = distance[start] + time

                # N번 시행 시 갱신된다면 음의 가중치가 존재한다는 것
                if i == N-1:
                    return 'YES'

    return 'NO'

INF = 1e9
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    route = []
    distance = [INF for _ in range(N + 1)]

    for _ in range(M):  # 그냥 경로는 양방향 그래프로
        a, b, t = map(int, input().split())
        route.append([a, b, t])
        route.append([b, a, t])

    for _ in range(W):  # 웜홀은 단방향 그래프로
        s, e, t = map(int, input().split())
        route.append([s, e, -t])

    print(bellman_ford())
