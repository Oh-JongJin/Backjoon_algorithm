count = int(input())
stack = []

for i in range(count):
    PS = str(input())
    for x in PS:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if '(' in stack:
                stack.pop()
            elif '(' not in stack or len(stack) >= 1:
                print('NO')
                break
    else:
        if len(stack) >= 1:
            print('NO')
        else:
            print('YES')
    stack = []
