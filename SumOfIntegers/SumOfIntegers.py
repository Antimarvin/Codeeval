__author__ = 'Antimarvin'

from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def sumOfDigits(number):
    total = 0
    for char in str(number):
        total += int(char)
    return total


def main():
    """
    Main execution
    """
    script, filename = argv

    inputs = [line for line in read_file_to_list(filename)]
    for i in inputs:
        cleanedi = i.rstrip('\n')
        print sumOfDigits(cleanedi)

if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert sumOfDigits('3058') == 16, "Failed 3058"
    assert sumOfDigits('125') == 8, "Failed 125" #FIXME
    main()