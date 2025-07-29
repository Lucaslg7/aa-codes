palavra = input().upper()

print(set(palavra))
if len(set(palavra)) == 26:
    print("YES")
else:
    print("NO")