__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def SelfDescribing(data):
    for i, x in enumerate(data):
        if data.count(str(i)) != int(x):
            return 0
    return 1



def main():
    """
    Main execution
    """
    script, filename = argv
    #filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(SelfDescribing(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert SelfDescribing("2020") == 1, "Failed 1"
    assert SelfDescribing("22") == 0, "Failed 7"
    assert SelfDescribing("1210") == 1, "Failed 22"

    main()