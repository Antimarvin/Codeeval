__author__ = 'Antimarvin'

from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def UniqueElements(data):
    result = data.split(",")
    result = sorted(set(result))
    return ','.join(result)


def main():
    """
    Main execution
    """
    script, filename = argv
    data = read_file_to_list(filename)

    for row in data:
        print(UniqueElements(row))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert UniqueElements("1,2,3,4,4,4,5,6,6") == "1,2,3,4,5,6", "Failed unique"
    assert UniqueElements("2,6,5,3,8,7") == "2,3,5,6,7,8", "Failed sort"
    assert UniqueElements("22,44,55") == "22,44,55", "Failed double digits"
    main()