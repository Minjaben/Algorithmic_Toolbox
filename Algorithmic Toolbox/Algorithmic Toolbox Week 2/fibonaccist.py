# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fiblist(n):
    F = ([0] * (n + 1))
    F[0] = 0
    F[1] = 1
    #print(*F, sep='\n')
    for i in range(2,n+1):
        F[i] = (F[i - 1] + F[i - 2])
       # print (F[i])
        #print ( str(i) + " = " + str(F[i]))
   # print (F[n])
    
    return (F[n])

n = int(input())
#print(calc_fib(n))
#print (n)
if (n == 0):
    print (0)
else:
    final = (fiblist(n))
    print (final)


"""
This is the stress test and naive to fast comparison.
#while True:
    #n = random.randint(1, 5) # Set the range of numbers in the list.
    #a = [0] * (n + 1)
    #for i in range(n):
    #   a[i] = random.randint(0,9) # Set the numerical range for each instance in the list a[].
    #h += 1
    #print(*a, sep='\n')
for i in range (n + 1):
    result1 = calc_fib(i+1)
    result2 = fiblist(i+1)

    if result1 == result2:
        print (str(i) + "OK")
    else:
        print ("Wrong answer: ", result1, result2)
        break

"""