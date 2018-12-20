# Uses python3
import math
new = int()
def lcm_naive(a, b):
    a = int(a)
    b = int(b)
    if a == 1: return b
    if b == 1: return a
    
    if gcdnum <= 50:
        #print (gcdnum)-(a*b)%gcdnum)
        return math.trunc(a/gcdnum) * b
        #return math.trunc(therightanswer)
    # for some reason I was getting an incorrect number if I changed this to int.
  #  if gap <= 10:
       # print ("It's working!! asdflkajsdf;dss")
   #     if b < a: return (b*a / (a/gap))
    #    if a < b: return (b*a / (b/gap))
    if a > b:
        new = b
    else: 
        new = a
        a = b
    for l in range(1, a*b + 1):
        #print ((new * l)
        if (new * l) % a == 0:
            return new * l

    #return a*b
#Greatest common divisor function:
def GCD(a,b):
    if b == 0:
        return a
    aprime = (a%b)
    return GCD(b, aprime)
"""    if a >= b:
        rem = (a % b)
        print (rem)
    else:
        rem = (b % a)
        a = b
    if rem > 0:
        GCD(a, rem)
        #print (a) #   print(*a, sep='\n')
    else:
        return a
"""
a, b = [int(x) for x in input().split()]
gcdnum = GCD(a,b)
print(lcm_naive(a, b))
#print(GCD(a,b))

