import sys

n = int(sys.stdin.readline())
f = [0] * 10001

for i in range(n):
    f[int(sys.stdin.readline())] += 1
for j in range(len(f)):
    if f[j] != 0:
        for k in range(f[j]):
            print(j)