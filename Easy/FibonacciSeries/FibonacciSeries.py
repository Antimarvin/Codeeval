__author__ = 'Antimarvin'

from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def fib(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number-1)+fib(number-2)

def main():
    """
    Main execution
    """
    script, filename = argv

    inputs = [line for line in read_file_to_list(filename)]
    for i in inputs:
        cleanedi = i.rstrip('\n')
        print fib(int(cleanedi))

if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert fib(0) == 0, "Failed 0"
    assert fib(1) == 1, "Failed 1"
    assert fib(5) == 5, "Failed 5"
    assert fib(12) == 144, "Failed 12"
    main()