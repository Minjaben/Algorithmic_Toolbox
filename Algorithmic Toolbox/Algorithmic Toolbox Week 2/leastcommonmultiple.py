#Uses python3

import sys
"""
Thought process for this problem:
If we use the same variables for the remainder of the greatest common divisor problem (different perhaps)...
If we use a loop to run through each iteration of multiples of a, and store each in an array corresponding to the amount, then we can compare the result for b.

SOLVED!
naivefct() was my original idea.
Unfortunately it's taking too long.


"""
#a, b = [int(x) for x in input().split()]
def naivefct(a,b):
    if a == 1:
        return b
    elif b == 1:
        return a
    aproducts = [0] * (a * b)
    aproducts[0] = a
    bproducts = [0] * (a * b)
    bproducts[0] = b
    step = 0
    #print(*bproducts, sep='\n')
    for i in range(0, len(aproducts)):
        aproducts[i] = (i+1) * a
        step += 1
       # print (str(i) + "is the element for " + str(aproducts[i]))
    step = 1
    for i in range(0, len(bproducts)):
        bproducts[i] = (i+1) * b
        #print (bproducts[i])
        for j in range(0, step):
            if ((bproducts[i] % aproducts[j])==0):
                #print(*bproducts, sep='\n')
                return bproducts[i]
            elif (aproducts[i] % bproducts[j]==0):
                return aproducts[i]
        step += 1
        
def fastfct(a,b):
    step = 1
    if (a - b) == abs(1):
        return (a * b)
    while True:
        if a < b:
            if a == 1:
                return b
            if (a * step) % b == 0:
                return (a * step)
            else:
                step += 1
        else:
            if b == 1:
                return a
            if (b * step) % a ==0:
                return (b * step)
            else:
                step += 1
        


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


        

#final = fastfct(a, b)
#print (final)

    
    
