# Uses python3
import sys
def sortbyratio(weights, values):
    ratios = [0]*n
    #print (*weights, sep='\n')
    for i in range(0, n):
        #print ("i is", i)
        ratios[i] = values[i]/weights[i]
        
    zipped = zip(ratios, values, weights)
    zipped = sorted(zipped, key=lambda x: x[0], reverse=True)
    ratiost, valuest, weightst = zip(*zipped)
    #print (type(ratiost))
    for i in range(len(values)):
        values[i] = int(valuest[i])
        weights[i] = int(weightst[i])
    #print (type(weights))
        
    return (weights, values)
def get_optimal_value(capacity, weights, values):
    finalval = 0
    a = 0
    roomleft = capacity
    for i in range(0, n):
        if roomleft == 0:
            return finalval
        a = min(weights[i],roomleft)
        #print(a)
        #print(values[i], weights[i])
        finalval += (a*(values[i]/weights[i]))
        roomleft -= a
        #weights[i] = "{:.10f}".format(weights[i])
        #print(type(weights[i]))
        #print(type(a))
       
        weights[i] = int(weights[i])-a
       # print ("i is ", i, ", finalval is ", finalval, "and roomleft for this iteration is now ", roomleft)
    # write your code here
   # print("It's working!")
    
    return finalval


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
   # print(values)
    weights = data[3:(2 * n + 2):2]
    weights, values = sortbyratio(weights, values)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
