import sys
input = sys.stdin.readline

N = int(input())
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

grid = [[0 for _ in range(N)] for _ in range(N)]  # 사과 표시

from collections import deque
grid_snake = deque()  # 뱀이 이동한 좌표를 저장하는 덱큐

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    grid[i - 1][j - 1] = 1  # 여기에 사과가 있어요

L = int(input())
change_direction = []
for _ in range(L):
    x, c = input().split()
    change_direction.append((int(x), c))  # 이때 방향 전환을 할 거에요

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 최초 뱀 위치 세팅
grid_snake.append((0, 0))
head_i, head_j, tail_i, tail_j = 0, 0, 0, 0

# 회전 정보 인덱스 세팅
change_index = 0

cur_dir = 0
time = 0
while True:
    time += 1
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    head_i = head_i + dx[cur_dir]
    head_j = head_j + dy[cur_dir]

    # 종료 조건: 만약 머리가 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not in_range(head_i, head_j) or (head_i, head_j) in grid_snake:
        break
    grid_snake.append((head_i, head_j))

    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if grid[head_i][head_j] == 1:
        grid[head_i][head_j] = 0

    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        tail_i, tail_j = grid_snake.popleft()

    if change_index < L:
        # 현재 시간에서 회전해야 하는지를 확인한다.
        change_time, change_dir = change_direction[change_index]
        if time == change_time:
            # X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻
            if change_dir == 'D':
                cur_dir = (cur_dir + 1) % 4
            else:
                cur_dir = (cur_dir - 1) % 4
            change_index += 1

print(time)
