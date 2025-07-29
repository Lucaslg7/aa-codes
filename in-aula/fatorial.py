# Pré processamento

n = int(input())
nums = [int(i) for i in input().split()]

fat = [1] * 31

for i in range(1, 31):
    fat[i] = fat[i-1] * i

for i in nums:
    print(fat[i], end=' ')

print()

