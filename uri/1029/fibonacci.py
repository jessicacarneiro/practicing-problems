MAX = 40

def fib(values, calls):
    values.append(0) # values[0]
    values.append(1) # values[1]

    calls.append(0) # calls[0]
    calls.append(0) # calls[1]
    calls.append(2) # calls[2]

    for i in range(2, MAX):
        values.append(values[i-1] + values[i-2])
    
    for i in range(3, MAX):
        calls.append(calls[i-1] + calls[i-2] + 2)

n = int(input())
cases = []

for i in range(0, n):
    cases.append(int(input()))

values = []
calls = []
fib(values, calls)

for i in range(0, n):
    print "fib({}) = {} calls = {}".format(cases[i], calls[cases[i]], \
                                           values[cases[i]])