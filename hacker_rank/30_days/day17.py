from math import sqrt

class Calculator:
    def power(self,a,b):
        try:
            y = sqrt(a)
            z = sqrt(b)
            return a ** b
        except Exception:
            return "n and p should be non-negative"

myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e