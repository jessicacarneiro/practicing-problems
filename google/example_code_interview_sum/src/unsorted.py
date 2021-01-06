import sys

def find_sum(numbers, total):
    """Return true if two numbers in an array
    exist such as they sum up to a specified total.

    Keyword arguments:
    numbers -- array of numbers
    total -- the total the sum should be equal to
    """
    complement = []
    for n in numbers:
        if n in complement:
            return True
        complement.append(total - n)
    return False

if __name__ == "__main__":
    numbers = sys.argv[1]
    total = sys.argv[2]
    print(find_sum(numbers, total))