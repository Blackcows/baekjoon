import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')

matrix = [[INF] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0  # 시작 도시와 도착 도시가 같은 경우는 없다.

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = min(c, matrix[a - 1][b - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for a in range(n):
    for b in range(n):
        if matrix[a][b] == INF:
            print("0",  end=" ")
        else:
            print(matrix[a][b], end=" ")
    print()
