import sys
input = sys.stdin.readline

txt = input()

word_set = set()

for i in range(len(txt)):
    for j in range(i+1, len(txt)):
        split_txt = txt[i:j]
        word_set.add(split_txt)

print(len(word_set))
