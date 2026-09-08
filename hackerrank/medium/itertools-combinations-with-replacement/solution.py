# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split()
S = sorted(S)
k = int(k)

for i in range(1, k + 1):
    for combination in combinations(S, i):
        print(''.join(combination))
