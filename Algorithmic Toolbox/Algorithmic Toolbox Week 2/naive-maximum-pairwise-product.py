# Uses python3
a,b = int(input()), int(input()) 
product = 0
for i in range(n):
   for j in range(i + 1, n):
       product = max(product, a[i] * a[j])
print(product)