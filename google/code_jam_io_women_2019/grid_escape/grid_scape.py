import sys
from quick_find import QuickFind

def conv_coord_to_number(row, col, n_row, n_col):
    if row == 0 or col == 0 or row > n_row or col > n_col:
        return 0
    return n_col * (row - 1) + col

def calc_neighbor(row, col, n_row, n_col, dir):
    if dir == "N":
        return conv_coord_to_number(row-1, col, n_row, n_col)
    elif dir == "E":
        return conv_coord_to_number(row, col+1, n_row, n_col)
    elif dir == "S":
        return conv_coord_to_number(row+1, col, n_row, n_col)
    elif dir == "W":
        return conv_coord_to_number(row, col-1, n_row, n_col)
    return -1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Usage: python grid_scape.py <file>")
     
    with open(sys.argv[1], "r") as f:
        first_line = f.readline()
        
        n_row, n_col = list(map(int, first_line.split()))
        qf = QuickFind(n_row*n_col + 1)
                
        row = 1
        for r in range(0, n_row):
            tokens = f.readline().split()
            
            col = 1
            for t in tokens:
                p = conv_coord_to_number(row, col, n_row, n_col)
                q = calc_neighbor(row, col, n_row, n_col, t)

                qf.union(p,q)
                
                col += 1

            row += 1
            
        count = 0
        for i in range(1, n_row*n_col+1):
            if qf.connected(0, i):
                count += 1
                print("#{} escaped.".format(i))
        
        print("a total of {} escaped.".format(count))
                
                
                
                