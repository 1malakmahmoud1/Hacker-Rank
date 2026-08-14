from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    d[word].append(str(i))

for _ in range(m):
    word = input().strip()
    if word in d:
        print(" ".join(d[word]))
    else:
        print("-1")