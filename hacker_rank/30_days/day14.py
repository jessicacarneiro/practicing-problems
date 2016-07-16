class Difference:
    def __init__(self, a):
        self.__elements = a

    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -100000
    
    def computeDifference(self):
        from math import fabs

        for i in xrange(len(self.__elements)-1):
            for j in xrange(i+1, len(self.__elements)):
                if fabs(self.__elements[i] - self.__elements[j]) > self.maximumDifference:
                    self.maximumDifference = int(fabs(self.__elements[i] - self.__elements[j]))
                   

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference