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

    inputs = [line for line in read_file_to_list(filename)]

    for i in inputs:
        #FIXME


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert bit_compare([86, 2, 3]) == True, "Failed 86, 2, 3" #FIXME
    assert bit_compare([125, 1, 2]) == False, "Failed 125, 1, 2" #FIXME
    main()