# Find approximate square root of 'x' using
# Newton-Raphson method

# Find 'x' such that x**2-24 is within epsilon of 0
epsilon = 0.0000000000001
k = 24.0
guess = k/2.0
iterations = 0

while abs(guess**2-k) >= epsilon:
    guess = guess - (guess**2-k)/(2*guess)
    iterations+=1;

print 'Square root of ', k, ' is about ', guess
print 'This took ', iterations, 'iterations of the loop'
