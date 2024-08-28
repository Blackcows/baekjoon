import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().strip())

k = K
stack = []
for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:  # stack top 보다 지금 비교하는 수가 더 크다면
        stack.pop()  # 뺄 수 있는 한 다 뺌
        k -= 1
    stack.append(num[i])
    # print(stack)  

ans = "".join(stack[:N-K])
print(ans)

