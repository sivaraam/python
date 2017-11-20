def Hanoi(n, s, t, b):
    if n == 1:
        print 'move disk from ', s, ' to  ', t
    else:
        Hanoi(n-1, s, b, t)
        Hanoi(1, s, t, b)
        Hanoi(n-1, b, t, s)

baseIndent = '    '
def HanoiPrint(n, s, t, b, indent):
    print indent + 'HanoiPrint called with: '
    print indent + 'Source: ', s, ' Target: ', t, ' Buffer: ', b
    if n == 1:
        print 'move disk from ', s, ' to  ', t
    else:
        HanoiPrint(n-1, s, b, t, indent+baseIndent)
        HanoiPrint(1, s, t, b, indent+baseIndent)
        HanoiPrint(n-1, b, t, s, indent+baseIndent)

HanoiPrint(3, 's', 't', 'b', '    ')
