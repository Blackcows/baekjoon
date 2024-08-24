import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    candidate = []
    for _ in range(N):
        candidate.append(list(map(int, input().split())))
    
    candidate.sort(key=lambda x: x[0])

    key = candidate[0][1]
    cnt = 1
    for i in range(1, N):
        # 더 앞 등수가 나왔다면
        if candidate[i][1] < key:
            key = candidate[i][1] # 해당 값을 key로 바꿈
            cnt += 1
            # 0번 인덱스로 정렬되어 있기 때문에, 1번 인덱스에서 더 앞쪽 값이 나오면 key 값을 바꿔줘야
            # 그 이후의 1번 인덱스에서 더 뒤쪽 값이 나온다면 그 사람은 뽑히지 않게 된다
    print(cnt)
