# encoding utf-8
initial, final = raw_input().split()
combinations = [[-2,-1], [-2,1], [-1,-2], [-1,2], \
                [1,  2], [1,-2], [2,  1], [2,-1]]

def generate_positions(initial):
    positions = []
    letter, number = ord(initial[0]), ord(initial[1])
    for c in combinations:
        l = chr(letter+c[0])
        n = chr(number+c[1])
        if l.isalpha() and n.isdigit() and int(n) > 0:
            positions.append(l+n)
    return positions

positions = generate_positions(initial)

if final in positions:
    print 'VALIDO'
else:
    print 'INVALIDO'