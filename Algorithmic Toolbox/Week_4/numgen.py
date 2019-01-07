import sys
import random
input = sys.stdin.read()
n = int(sys.argv[1])
print(n)
for i in range(0, n):
    print (random.randint(1, 10**9), end=" ")
