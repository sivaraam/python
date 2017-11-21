import math

class shape:
    def area(self):
        raise NotImplementedError
    
    def __lt__(self, other):
        return self.area() < other.area()
##
##    def __gt__(self, other):
##        return self.area() > other.area()


class rectangle(shape):
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def area(self):
        return self.l * self.h
    
    def __lt__(self, other):
        if self.l != other.l:
            return self.l < other.l
        else:
            return self.h < other.h

class circle(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return (4/3)*math.pi*r*r

    def __lt__(self, other):
        return self.r < other.r
    
