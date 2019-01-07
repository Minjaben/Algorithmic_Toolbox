# Uses python3
import sys

def get_majority_element(a, left, right):
    """
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    alen = len(a)
    midpoint = int(alen/2)
    if a[0] == a[midpoint]:
        return 1
    #write your code here
    return -1
    """
    for x in a:
        if instances > int(len(a)/2):
            return 1
    return -1

def most_common(lst):

    majcand = max(set(lst), key=lst.count)
    instances = a.count(majcand)
    return (majcand, instances)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a.sort()
    majcand, instances = most_common(a)
    #print (majcand, instances)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)




""" For a n/2 section of a list of integers n,
if one side has a majority,
count the instances of that number in the whole string and check if it is greater than n/2"""
