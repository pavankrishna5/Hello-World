# Uses python3
import sys

def get_fibonacci_last_digit(n):
    l=[0,1]
    for i in range(2,n+1):
        l.append((l[i-1]+l[i-2]) % 10)
    return (l[n])

input = input()
n = int(input)
print(get_fibonacci_last_digit(n))
