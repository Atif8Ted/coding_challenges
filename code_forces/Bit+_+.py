no_of_operation = int(input())
x=0
for i in range(no_of_operation):
    operation = input()
    if '++' in operation:
        x = x+1
    else:
        x = x-1

print(x)