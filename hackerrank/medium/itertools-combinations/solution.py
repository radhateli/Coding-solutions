# Enter your code here. Read input from STDIN. Print output to STDOUT
S, k = input().split()
k = int(k)

S = sorted(S)

def generate(current, remaining):
    if len(current) == k:
        print(''.join(current))
        return

    for i in range(len(remaining)):
        generate(current + [remaining[i]], 
                 remaining[:i] + remaining[i+1:])

generate([], S)
