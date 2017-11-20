# Find approximate square root of 'x' using
# bisection method

# Find 'x' such that x**2-24 is within epsilon of 0
epsilon = 0.0000000000001
k = 24.0
low = 0.0
high = max(1, k) # To avoid issue of finding square root of numbers in range [0,1)
ans = (low+high)/2
iterations = 0

while abs(ans**2-k) >= epsilon and ans <= k:
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (low+high)/2
    iterations+=1;

print 'Square root of ', k, ' is about ', ans
print 'This took ', iterations, 'iterations of the loop'
