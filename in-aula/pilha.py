entrada = input()

fila = []
for c in entrada:
    if len(fila) == 0:
        if c in ')]}':
            print('NO')
            exit(0)
    
    if c in '([{':
        fila.append(c)
    else:
        if c == ')' and fila[-1] == '(':
            fila.pop() 
        elif c == ']' and fila[-1] == '[':
            fila.pop()
        elif c == '}' and fila[-1] == '{':
            fila.pop()       
        else:
            print('NO')
            exit(0)
    

if len(fila) == 0:
    print('YES')
else:
    print('NO')