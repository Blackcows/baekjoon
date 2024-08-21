import sys
input = sys.stdin.readline

n = int(input())

alpha = {}

words = []
for _ in range(n):
    txt = input().strip()
    words.append(txt)
    for i in range(len(txt)):
        if txt[i] not in alpha:
            alpha[txt[i]] = 10 ** (len(txt)-1-i)
        else:
            alpha[txt[i]] += 10 ** (len(txt) - 1 - i)

alpha = dict(sorted(alpha.items(), key=lambda x: x[1], reverse=True))

ans = 0
num = 9
for char in alpha:
    ans += alpha[char] * num
    num -= 1

print(ans)
