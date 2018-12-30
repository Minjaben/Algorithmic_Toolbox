#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

def sortdata(a,b):
    # In this function we need to sort the revenue per click (a[i]) in descending order,
    # then sort the amount paid per click (b[i]), and return both lists to reassign the original lists as their ordered permutations.
    asorted = sorted(a, reverse=True)
    #print(asorted)
    bsorted = sorted(b, reverse=True)
    #print(bsorted)
    return (asorted, bsorted)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    a, b = sortdata(a,b)
    print(max_dot_product(a, b))
    
