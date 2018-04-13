import math


class shape:
    def area(self):
        raise NotImplementedError

    def __lt__(self, other):
        return self.area() < other.area()

#    if __gt__ is not defined but __lt__ is defined then the expression
#    s1 > s2 results in __lt__ being called (as if the expression was
#    s2 < s1) and vice versa.
#    def __gt__(self, other):
#        return self.area() > other.area()


class rectangle(shape):
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def area(self):
        return self.l * self.h

    def __lt__(self, other):
        if (type(self) == type(other)):
            if self.l != other.l:
                return self.l < other.l
            else:
                return self.h < other.h
        else:
            return super(rectangle, self).__lt__(other)


class circle(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return (4/3) * math.pi * self.r * self.r

    def __lt__(self, other):
        if (type(self) == type(other)):
            return self.r < other.r
        else:
            return super(circle, self).__lt__(other)
