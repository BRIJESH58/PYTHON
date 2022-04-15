from itertools import combinations

numbers = [int(n) for n in input().split()]
k = int(input())
count = 0
for i in range(1, len(numbers)+1):
    for c in combinations(numbers, i):
        if sum(c) == k:
            count += 1
print(count)
