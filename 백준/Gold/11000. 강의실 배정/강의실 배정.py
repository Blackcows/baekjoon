import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort() # 시작 시간을 기준으로 정렬

import heapq
queue = [arr[0][1]]

for i in range(1, n):
    if arr[i][0] < queue[0]:  #  다음 회의 시작 시간이 직전 회의 종료 시간보다 빠르면
        heapq.heappush(queue, arr[i][1])  # heapq의 0번 인덱스가 변경
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, arr[i][1])

print(len(queue))