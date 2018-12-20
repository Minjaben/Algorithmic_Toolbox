#Uses python3
n = int(input())       # Comment out for class function.
#a = [None] * n
"""for i in range(n):     #Automatically generated array for values up to n.
    a[i] = int(i+1)
"""
a = [int(x) for x in input().split()] #The user-inputted array option.
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
#print (index1, " ", index2)  
#print ("n equals", n)
final = (a[index1] * a[index2])
print(final)   