__author__ = 'Antimarvin'
from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def make_len_list(line):
    return [line, len(line)]


def main():
    """
    Main execution
    """
    # script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)
    data.reverse()
    quantity = int(data.pop().rstrip())
    len_list = []
    for row in data:
        if not row.isspace():
            len_list.append(make_len_list(row.rstrip()))
    len_list.sort(key=lambda line: line[1],reverse=True)
    for i in range(quantity):
        print(len_list[i][0])


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    main()
