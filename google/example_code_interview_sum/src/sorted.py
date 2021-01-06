import sys

def find_sum(numbers, total):
    """Return true (in O(n)) if two numbers in a sorted
    array exist such as they sum up to a specified total.

    Keyword arguments:
    numbers -- array of numbers (sorted)
    total -- the total the sum should be equal to
    """
    i = 0
    j = len(numbers) - 1
    
    while(i < j):
        if (numbers[i] + numbers[j] < total):
            print('here: {} {}'.format(numbers[i], numbers[j]))
            i += 1
        elif (numbers[i] + numbers[j] > total):
            print('here: {} {}'.format(numbers[i], numbers[j]))
            j -= 1
        else:
            print('here: {} {}'.format(numbers[i], numbers[j]))
            return True
    return False


if __name__ == "__main__":
    stripped = sys.argv[1].replace('[','').replace(']', '')

    numbers = map(int, stripped.split(','))
    # total = int(sys.argv[2])
    print(numbers)
    # print(type(numbers))
    # print(total)
    # print(find_sum(numbers, total))