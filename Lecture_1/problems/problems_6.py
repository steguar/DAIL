# problem 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# problem 2
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# problem 3
center = Point(150, 100)   
circle = Circle(center,75)

# problem 4
def distance(p, q):
    d = ((p.x-q.x)**2+(p.y-q.y)**2)**0.5
    return d

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def contains_point(self,p):
        return distance(self.center,p)<=self.radius
    
# problem 5
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

# problem 6
def add_times(t1, t2):
    return Time(t1.h+t2.h,t1.m+t2.m,t1.s+t2.s)
    
# problem 7
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    def __add__(self, t):
        tnew = add_times(self,t)
        self.h = tnew.h
        self.m = tnew.m
        self.s = tnew.s

# problem 8
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    def __add__(self, t):
        tnew = add_times(self,t)
        self.h = tnew.h
        self.m = tnew.m
        self.s = tnew.s
    def time_to_int(self):
        return self.s+60*self.m+3600*self.h

# problem 9
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    def __add__(self, t):
        tnew = add_times(self,t)
        self.h = tnew.h
        self.m = tnew.m
        self.s = tnew.s
    def time_to_int(self):
        return self.s+60*self.m+3600*self.h
    def int_to_time(s):
        h,s = s//3600,s%3600
        m,s = s//60,s%60
        return Time(h,m,s)

# problem 9
class Time:
    def __init__(self, h=0, m=0, s=0):
        if s>60:
            t = int_to_time(s)
        self.h = h+t.h
        self.m = m+t.m
        self.s = s+t.s
    def __add__(self, t):
        tnew = add_times(self,t)
        self.h = tnew.h
        self.m = tnew.m
        self.s = tnew.s
    def time_to_int(self):
        return self.s+60*self.m+3600*self.h
    def int_to_time(s):
        h,s = s//3600,s%3600
        m,s = s//60,s%60
        return Time(h,m,s)
