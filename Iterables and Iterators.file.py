from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))

favorable = sum(1 for comb in all_combinations if 'a' in comb)

print(round(favorable / len(all_combinations), 4))