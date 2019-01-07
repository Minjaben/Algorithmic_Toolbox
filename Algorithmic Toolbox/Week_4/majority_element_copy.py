# Uses python3
import sys
def get_majority_element(a, master_a):
    # if left == right:
    #    return -1
    #if left + 1 == right:
    #    return a[left]

    #print(len(a))
    alen = len(a)
    if alen == 1:
        print("returning success length 1")
        return (1, a[0])

    if alen == 2:
        if a[0] == a[1]:
            print("Returning success length 2")
            return (1, a[0])
        else:
            print("Returning failure")
            return (0, a[0])

    #if alen == 3:
    #    print (a)
    #    if a[0] == a[1] or a[0] == a[2]:
    #        return (1, a[0])
    #    elif a[1] == a[2]:
    #        #print ("success")
    #        return (1, a[1])
    #    else:
    #        return (0, a[0])
    midpoint = int(alen/2)
    left = a[:midpoint]
    right = a[midpoint:]
    print(left)
    print(right)
    return get_majority_element(left, master_a)
    #rightres = (0, 0)
    #rightres = get_majority_element(right, master_a)
    #if leftres[0] == 1:
    #    ct = countmaj(master_a, leftres[1])
    #    print ("ct left equals", ct)
    #    if ct == 1:
    #        return (1, 0)
    return get_majority_element(right, master_a)
    #if rightres[0] == 1:
    #    ct = countmaj(master_a, rightres[1])
    #    print ("ct right equals", ct)
    #    if ct == 1:
    #        return (1, 0)
            #break
    #return (leftres[1], rightres[1])



def countmaj(a, majnum):
    count = 0
    for x in range(0,n):
        if a[x] == majnum:
            count += 1
            #print (count, " is the count.")
        if count > len(a)/2:
            #print ("successful return")
            return 1
    return 0

    #else:
    #    return 0



    #write your code here

    #return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    master_a = a
    alen = len(a)
    midpoint = int(alen/2)
    left = a[0:midpoint]
    right = a[midpoint:]
    print(left)
    print(right)
    # a.sort()
    # print(*a, sep=' ')
    leftresult = get_majority_element(left, master_a)
    print(leftresult, "is the left result.")
    rightresult = get_majority_element(right, master_a)
    print(rightresult, "is the right result.")
    if leftresult[0] == 1:
         left_search_res = countmaj(master_a, rightresult)
         if left_search_res[0] == 1:
             print (1)
    elif rightresult == 1:
         right_search_res = countmaj(master_a, leftresult)
         print (right_search_res[0])
    else:
        print (0)

    #print (result)
    # print (result[1])
    # if result == 1:
    #    countmaj(a, majnum)

    #else:
    #    print(0)


# ASSUMPTION IS NOT NECESSARILY TRUE ==> CONFUSING
# Switch the check from the inside of the loop to some time outsideself.
# Crazy!!! Argh!

#
#
#
