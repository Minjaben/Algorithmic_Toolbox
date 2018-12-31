# Uses python3
import sys

def binary_search(a, x, left, right):
    #print (x)
    #left, right = 0, (len(a)-1)
    #print (left, "is the low value")
    #print (right, "is the high value")
    if (left > right):
        return (-1)
    #print (a[left], " is the value for a[left]")
    mid = int(left + (right-left)/2)
    #print (mid)
    if x == a[mid]:
        #print (mid)
        return mid
    elif x < a[mid]:
        right = (mid - 1)
        return binary_search(a, x, left, right)
        print("less than mid")
    else:
        #print (a[mid+1])
        left = (mid + 1)
        return binary_search(a, x, left, right)
        print("more than mid")
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    left, right = 0, (len(a)-1)
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(x)
        print(binary_search(a, x, left, right), end = ' ')
        #print(linear_search(a, x), end = ' ')
