# Uses python3
# This program attempts to calculate the greatest integer d that divides both a and b.

a, b = [int(x) for x in input().split()]
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
gcd_val = GCD(a,b)
print (gcd_val)

        