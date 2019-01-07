# Uses python3
import sys
import random
sys.setrecursionlimit(15000)

def partition3buggy(a, l, r):
    x = a[l]
    #print (x)
    jr = l;
    jl = l;
    r = l;
    # Why is l + 1 and r + 1 used instead of l and r here?
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            jr +=1
            a[i], a[jr] = a[jr], a[i]
    a[l], a[jr] = a[jr], a[l]
    match = true
    print (l + 1, r - 1)
    for i in range(l + 1, r - 1):
        print ("a[i] is ", a[i], "and a[jr] is ", a[jr])
        if a[i] == a[jr]:
            jl = i
            return jl, jr
    #print (match)
    #print ("a[l] is ", a[l], "and a[j] is ", a[j])
    #print ("jl is ", jl, "and jr is ", jr)
    return jl, jr
    #Nothing happens when pass executes. Returns null.
    pass

def partition3(a, l, r):
    x = a[l]
    i = l - 1
    j = l
    switch = True
    for i in range (l + 1, r + 1):


"""        Below is deprecated non-working code.
    while (switch == True):
        #print(i, j)
        while (a[j] > x):
            j -= 1
        #    print(A[j], x)
        #print("Moving to A[i]")
        while (A[i] < x):
            i += 1
            #print(A[i], x)
        #print (i, j)
        if i < j:
            A[i], A[j] = A[j], A[i]
            #switch = False
        else:
            return j
        #return j
"""



def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    (m) = partition3(a, l, r)
    #m = partition2(a, l, r)
    #print (m)
    #if (m-l) < (r-m):
        #l = m + 1
    randomized_quick_sort(a, l, m - 1);

    #else:
        #r = m - 1
    randomized_quick_sort(a, m + 1, r);



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
