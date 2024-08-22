import sys
input = sys.stdin.readline

# 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K
N, M, x, y, K = map(int, input().split())
def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

grid = [list(map(int, input().split())) for _ in range(N)]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

def spin(direction):
    global dice
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    if direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    if direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    if direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

commands = list(map(int, input().split()))

# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]

    if not in_range(nx, ny):
        continue

    x, y = nx, ny

    spin(command)

    if grid[x][y] == 0:
        grid[x][y] = dice[5]
    else:
        dice[5] = grid[x][y]
        grid[x][y] = 0

    print(dice[0])
