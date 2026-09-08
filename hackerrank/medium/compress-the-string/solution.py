# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = input()

for key, group in groupby(S):
    print((len(list(group)), int(key)), end=" ")
