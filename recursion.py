
# Factorial using Recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print('Enter a number to find factorial')
num=int(input())
result=fact(num)
print('The factorial of',num,'is',result)
