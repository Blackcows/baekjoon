import sys
input = sys.stdin.readline

n, k = map(int, input().split())
gems = []

for _ in range(n):
    gems.append(list(map(int, input().split())))

bags = []
for _ in range(k):
    bags.append(int(input()))

gems.sort(key=lambda x: (x[0], -x[1]))  # 보석 무게를 기준으로 오름차순, 보석 가치를 기준으로 내림차순(음수)
bags.sort()  # 가방 무게 오름차순 정렬 -> 가장 가벼운 보석부터 순서대로 넣기

import heapq
queue = []
total = 0

for bag in bags:
    # 가방의 최대 무게보다 현재 담은 보석 수가 적다면 더 담을 수 있음
    while gems and gems[0][0] <= bag:
        heapq.heappush(queue, -gems[0][1]) # 가격을 최대 힙에 저장하고
        heapq.heappop(gems) # 가격 저장한 보석은 삭제

    if queue: # 담을 수 있는 보석을 다 저장했으면
        total += -heapq.heappop(queue) # 제일 가치가 높은 가격부터 누적

print(total)