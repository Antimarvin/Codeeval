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


def bit_compare(i):
    value, p1, p2 = i

    rev_bin_value = bin(value)[::-1]
    if rev_bin_value[p1-1] == rev_bin_value[p2-1]:
        return True
    return False


def main():
    """
    Main execution
    """
    script, filename = argv

    inputs = []
    for line in read_file_to_list(filename):
        inputs.append(string_to_list(line))

    for i in inputs:
        print str(bit_compare(i)).lower()


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert bit_compare([86, 2, 3]) == True, "Failed 86, 2, 3"
    assert bit_compare([125, 1, 2]) == False, "Failed 125, 1, 2"
    main()