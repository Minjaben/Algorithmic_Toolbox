# Uses python3
import sys
def get_majority_element(a):
    #Input: Array a of objects.
    #Output: Majority element of a.
    n = len(a)
    if n == 1:
        return a[0]
    k = int(n/2)
    leftlist = a[:k]
    rightlist = a[k:]
    elementsubl = get_majority_element(leftlist)
    elementsubr = get_majority_element(rightlist)
    if elementsubl == elementsubr:
        return elementsubl
    lcount = GetFrequency(a, elementsubl)
    rcount = GetFrequency(a, elementsubr)
    if lcount > k:
        return elementsubl
    elif rcount > k:
        return elementsubr
    else: return -1

def GetFrequency(a, majnum):
    #Counts and returns the instances of majnum in list a
    count = 0
    for x in range(0,len(a)):
        if a[x] == majnum:
            count += 1
            #print (count, " is the count.")
    return count
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if (get_majority_element(a)) != -1:
        print(1)
    else: print(0)
