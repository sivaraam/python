called = 0

def ackermann(m, n):
    global called
    called += 1
    
    if m < 0:
        raise ValueError, "invaid 'm' value"
    
    if m == 0:
        return n+1

    if m > 0 and n == 0:
        return ackermann(m-1, 1)

    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

def test_ackermann(m, n):
    global called
    called = 0
    print ackermann(m, n)
    print "Number of times ackermann was called: ", called
    print
    
test_ackermann(3, 4)
test_ackermann(3, 6)
# print ackermann(3, 7) # inflection point for m=3, exceeds maximum recursion depth
# print ackermann(10, 5) # exceeds maximum recursion depth
