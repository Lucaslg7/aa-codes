n, q = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

somas = [0] * (n + 1)
for i in range(1 ,n+1):
    somas[i] = somas[i-1] + nums[i-1]
print(somas)

for i in range(q):
    a, b = [int(i) for i in input().split()]