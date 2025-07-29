n, q = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

somas = [0] * (len(nums) + 1)

for i in range(1, len(nums) + 1):
    somas[i] = somas[i-1] + nums[i-1]
print(somas)

for i in range(q):
    l, r = [int(i) for i in input().split()]
    print(somas[r] - somas[l-1])