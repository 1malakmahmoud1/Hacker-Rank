from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]
word_counts = Counter(words)

print(len(word_counts))
print(*word_counts.values())