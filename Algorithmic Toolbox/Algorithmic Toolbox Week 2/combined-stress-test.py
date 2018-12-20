#Uses python3
#This program generates 
import random
# A more efficient algorithm 
def fastpairwise(a):
    #n = int(input())       # Comment out for class function.
    #a = [None] * n
    """for i in range(n):     #Automatically generated array for values up to n.
        a[i] = int(i+1)
    """
    #a = [int(x) for x in input().split()] #The user-inputted array option.
    index1 = 0
    for i in range(n):
        if a[i] > a[index1]:
            index1 = i
    if (index1 == 0):
        index2 = 1
    else:
        index2 = 0
    for i in range(1, n):
        if (i != index1) and (a[i] > a[index2]):
            index2 = i
    print (index1, " ", index2)  
    print ("n equals", n)
    final = (a[index1] * a[index2])
    return (final)   
    
def naivepairwise(a):
   #  n = int(input())        # Comment out for class function.
    #a = [int(x) for x in input().split()]
    product = 0
    for i in range(n):
       for j in range(i + 1, n):
           product = max(product, a[i] * a[j])
    return (product)
    
    
    """ Negative Numbers.
    Unrequested input that's non-integers, etc.
    None
    Unit tests.
    
    
    """
    
    
    
#h = 0
while True:
    n = random.randint(1, 5) # Set the range of numbers in the list.
    a = [0] * (n + 1)
    for i in range(n):
        a[i] = random.randint(0,9) # Set the numerical range for each instance in the list a[].
    #h += 1
    print(*a, sep='\n')
    result1 = naivepairwise (a)
    result2 = fastpairwise (a)

    if result1 == result2:
        print ("OK")
    else:
        print ("Wrong answer: ", result1, result2)
        break

