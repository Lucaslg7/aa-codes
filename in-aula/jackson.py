import heapq as h

n = int(input())

f = []
for i in range(n):
    q = input()
    if q[0] == "1":
        q = q.split()
        h.heappush(f, -int(q[1]))
    else:
        h.heappop(f)

print(-f[0])