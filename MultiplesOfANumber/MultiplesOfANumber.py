__author__ = 'Antimarvin'

from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def string_to_list(instring):
    result = []
    for n in instring.split(','):
        result.append(int(n))
    return result


def get_smallest_multiple(i):
    bot_limit, multiple = i
    while True:
        multiple += multiple
        if multiple >= bot_limit:
            return multiple


def main():
    """
    Main execution
    """
    script, filename = argv

    inputs = []
    for line in read_file_to_list(filename):
        inputs.append(string_to_list(line))

    for i in inputs:
        print get_smallest_multiple(i)


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert get_smallest_multiple([13, 8]) == 16, "Failed 13,8"
    assert get_smallest_multiple([17, 16]) == 32, "Failed 18,16"

    main()