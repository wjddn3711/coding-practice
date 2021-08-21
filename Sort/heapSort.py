import heapq as hq
n = int(input())
ar = []
for i in range(n):
    hq.heappush(ar,int(input()))

while ar:
    print(hq.heappop(ar))


