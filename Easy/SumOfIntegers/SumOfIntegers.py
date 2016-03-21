__author__ = 'Antimarvin'

from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def main():
    """
    Main execution
    """
    script, filename = argv
    total = 0

    inputs = [line for line in read_file_to_list(filename)]
    for i in inputs:
        cleanedi = i.rstrip('\n')
        total += int(cleanedi)
    print total

if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    main()