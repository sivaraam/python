x = 0.0
for i in range(10):
    x = x + 0.1
if abs(x - 10*0.1) < 0.0001:
    print x, '= 1.0'
else:
    print x, 'is not 1.0'