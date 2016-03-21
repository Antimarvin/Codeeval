__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def NmodM(data):
    numerator, denominator = data.split(',')
    numerator, denominator = int(numerator), int(denominator)
    result = numerator - (denominator * int(numerator/denominator))

    return result

def main():
    """
    Main execution
    """
    #script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(NmodM(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert NmodM("20,6") == 2, "Failed"
    assert NmodM("2,3") == 2, "Failed"

    main()