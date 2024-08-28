import sys
input = sys.stdin.readline

A, B = map(int, input().split())

temp = B
count = 0
while True:
    if temp <= A:
        break

    if temp % 2 == 0:  # 쩍수면 2로 나눌 수 있음
        temp //= 2
    elif temp % 10 == 1:  # 끝자리가 1이면 1을 뺄 수 있음
        temp //= 10
    else:
        break

    count += 1

if temp == A:
    print(count + 1)
else:
    print(-1)
