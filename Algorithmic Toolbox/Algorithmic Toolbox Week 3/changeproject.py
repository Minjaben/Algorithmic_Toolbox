# Uses python3
import sys
def get_change(m):
    #For testing purposes:
    coincount = 0
   # print (m + "is executing the function.")
    while m > 0:
        if m >= 10:
            m -= 10
            coincount += 1
        elif m >= 5:
            m -= 5
            coincount += 1
        else:
            m -= 1
            coincount += 1
    return coincount


m = int(input())
#print (m)
print(get_change(m))