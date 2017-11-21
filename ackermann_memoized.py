##known = {}
##called = 0
##dememoized_calls = 0

def ackermann_memoized(m, n):
    global called, dememoized_calls
    called += 1
    
    if m < 0:
        raise ValueError, "invaid 'm' value"

    if (m, n) in known:
        return known[(m, n)]

    dememoized_calls += 1
    
    if m == 0:
        return n+1

    if m > 0 and n == 0:
        res = ackermann_memoized(m-1, 1)
        known [(m, n)] = res
        return res

    if m > 0 and n > 0:
        res = ackermann_memoized(m-1, ackermann_memoized(m, n-1))
        known [(m, n)] = res
        return res

def test_ackermann_memoized(m, n):
    global known, called, dememoized_calls
    known = {}
    called = 0
    dememoized_calls = 0
    print ackermann_memoized(m, n)
    print "Number of times ackermann_memoized was called: ", called
    print "Calls avoided dues to memoization: ", called - dememoized_calls
    print

test_ackermann_memoized(3, 4)
test_ackermann_memoized(3, 8)
test_ackermann_memoized(3, 9)
# test_ackermann_memoized(3, 9) # inflection point for m=3, exceeds maximum recursion depth
# exceeds maximum recursion depth
# test_ackermann_memoized(10, 4)
# test_ackermann_memoized(4, 1)
