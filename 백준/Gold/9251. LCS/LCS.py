import sys
input = sys.stdin.readline

txt_1 = input().strip()
txt_2 = input().strip()

dp = [[0 for _ in range(len(txt_2) + 1)] for _ in range(len(txt_1) + 1)]

for i in range(1, len(txt_1) + 1):
    for j in range(1, len(txt_2) + 1):
        if txt_1[i-1] == txt_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
