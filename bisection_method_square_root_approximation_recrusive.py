def rec_sqrt_bisection(x, epsilon, low = None, high = None):
    # Initialise low and high for first run
    if low == None:
        low = 0.0
    if high == None:
        high = max(x, 1)
    midpoint = (low+high)/2.0

    if abs(midpoint**2 - x) < epsilon : #or midpoint > x:
        return midpoint
    else:
        if midpoint**2 < x:
            return rec_sqrt_bisection(x, epsilon, midpoint, high)
        elif midpoint**2 > x:
            return rec_sqrt_bisection(x, epsilon, low, midpoint)


epsilon = 0.000001
print "Square root of 0.0098: ", rec_sqrt_bisection(0.0098, epsilon)
print "Square root of 0.64: ", rec_sqrt_bisection(0.64, epsilon)
print "Square root of 2: ", rec_sqrt_bisection(2, epsilon)
print "Square root of 5: ", rec_sqrt_bisection(5, epsilon)
print "Square root of 25: ", rec_sqrt_bisection(25, epsilon)
print "Square root of 7777: ", rec_sqrt_bisection(77777, epsilon)
##print "Square root of -10: ", rec_sqrt_bisection(-10, epsilon)
