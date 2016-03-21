__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def HappyNumbers(data):
    tempi = data
    numi = 0
    for i in range(0,200):
        for d in tempi:
            d = int(d)
            numi += d*d
        if numi == 1:
            return 1
        tempi = str(numi)
        numi = 0

    return 0


def main():
    """
    Main execution
    """
    script, filename = argv
    #filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(HappyNumbers(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert HappyNumbers("1") == 1, "Failed 1"
    assert HappyNumbers("7") == 1, "Failed 7"
    assert HappyNumbers("22") == 0, "Failed 22"

    main()