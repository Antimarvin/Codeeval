__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def RightmostChar(data):
    searchString, key = data.split(',')
    result = -1
    for i, x in enumerate(searchString):
        if x == key:
            result = i
    return result


def main():
    """
    Main execution
    """
    script, filename = argv
    #filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(RightmostChar(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert RightmostChar("Hello World,r") == 8, "Failed base"
    assert RightmostChar("Hello CodeEval,E") == 10, "Failed lowercase test"

    main()