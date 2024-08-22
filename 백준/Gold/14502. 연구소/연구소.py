import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

from collections import deque

lab = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def run_bfs(grid):
    # 각 경우에 대해 bfs
    def bfs():
        while queue:
            x, y = queue.popleft()
            grid[x][y] = 2

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if in_range(nx, ny) and grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    def cal_safezone(grid):
        count = 0
        for i in range(n):
            count += grid[i].count(0)
        return count

    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
    bfs()

    result = cal_safezone(grid)

    global ans
    ans = max(ans, result)

import copy
# 가벽 3개를 세우는 경우의 수를 브루트포스로 다 계산
ans = 0
walls = []

def makewall(walls, cnt):
    if cnt == 3:
        temp_lab = copy.deepcopy(lab)
        for wall in walls:
            r, c = wall
            temp_lab[r][c] = 1
        run_bfs(temp_lab)
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0 and (i, j) not in walls:
                walls.append((i, j))
                makewall(walls, cnt + 1)
                walls.remove((i, j))

makewall(walls, 0)

print(ans)