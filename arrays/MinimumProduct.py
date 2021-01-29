#minimum product subset array.

def minProductSubset(a,n):
    if(n==1):
        return a[0]
    #Find count of negative numbers,
    #count of zeros, maximum valued
    #negative number, minimum valued
    #positive number and product
    #of non-zero numbers
    max_neg = float('-inf')
    min_pos = float('inf')
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(0,n):

        if(a[i] == 0):
            count_zero += 1
            continue
        if(a[i]<0):
            count_neg += 1
            max_neg = max(max_neg, a[i])
        if(a[i]>0):
            min_pos = min(min_pos, a[i])
        prod = prod * a[i]
    if((count_neg & 1) == 0 and count_neg != 0):
        # Otherwise resulst is  product of
        # al non-zeros divided by
        # maximm valued nagtive.
        prod = int(prod/ max_neg)
    return prod
#this is the logic of the decade.
a = [-1,-1,-2,4,3]
n = len(a)
print(minProductSubset(a,n))
        
            
