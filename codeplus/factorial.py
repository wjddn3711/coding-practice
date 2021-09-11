import sys
# input = sys.stdin.readline()

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

n=int(input())
stack=[]
target=str(factorial(n))
for i in reversed(range(len(target))):
    if target[i]=='0':
        stack.append(target[i])
    else:
        break
print(len(stack))