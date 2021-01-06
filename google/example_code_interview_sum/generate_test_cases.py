import sys
from random import randint

MAX_ARRAY_ELEMENT = 10000
MAX_ARRAY_SIZE = 50000

def generate_list_numbers(max, size, sorted=False):
    """Generate a list of random numbers given a list
    size and a maximum value for the elements.

    Keyword arguments:
    max -- the maximum value for an element
    size -- the size of the list generated
    sorted -- if list should be sorted (default = False)
    """
    numbers = []
    for i in range(0, size):
        numbers.append(randint(0,max))
    if sorted:
        numbers.sort()
    return numbers

def generate_test_file(file, max, size, sorted=True):
    """Generate test file with one line, following the format
    array between square-brackets followed by an integer with
    a comma between them.
    [ n, n, .. , n], n

    Keyword arguments:
    file -- name of the file to be written
    max -- maximum value to be generated in the array
    size -- maximum array size
    sorted -- if array should be sorted (default = True)
    """
    f = open(file, 'w')
    s = randint(0,max)
    n = generate_list_numbers(randint(0,max), randint(1,size), sorted)
    f.write('{} {}'.format(n, s))
    f.close()

def create_test_files(total_files, sorted=True):
    """Create test files.

    Keyword arguments:
    total_files -- number of test files to be created
    sorted -- if array should be sorted (default = True)
    """
    for i in range(0, total_files):
        filename = ''
        if sorted:
            filename = 'test/sorted/test{}'.format(i)
        else:
            filename = 'test/unsorted/test{}'.format(i)

        max = randint(0, MAX_ARRAY_ELEMENT)
        size = randint(1, MAX_ARRAY_SIZE)

        generate_test_file(filename, max, size, sorted)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        total_files = int(sys.argv[1])
        sorted = bool(sys.argv[2] == 'True')
        create_test_files = create_test_files(total_files, sorted)
    elif len(sys.argv) > 1:
        total_files = sys.argv[1]
        create_test_files = create_test_files(total_files)
    else:
        print('Usage: python generate_test_cases [total_files]')
        print('Usage: python generate_test_cases [total_files] [sorted]')