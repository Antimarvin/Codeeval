__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def is_armstrong(data):
    armstrong_total = 0
    for d in data:
        armstrong_total += int(d) ** len(data)
    if int(data) == armstrong_total:
        return True
    else:
        return False


def main():
    """
    Main execution
    """
    #script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(is_armstrong(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    main()