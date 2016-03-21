__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def HexToDecimal(data):
    return int(data,16)

def main():
    """
    Main execution
    """
    #script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(HexToDecimal(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert HexToDecimal("9f") == 159, "Failed"
    assert HexToDecimal("11") == 17, "Failed"

    main()

for