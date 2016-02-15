__author__ = 'Antimarvin'
from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def BeautifulStrings(data):
    data =data.upper()
    data = ''.join(c for c in data if c.isalpha())
    print(data)
    keys = set(data)
    values = []
    beautynum = 26
    total = 0
    for k in keys:
        values.append([k,data.count(k)])
    values.sort(key=lambda letter: letter[1], reverse=True)
    for v in values:
        total += v[1] * beautynum
        beautynum -= 1
    print(values)
    return total


def main():
    """
    Main execution
    """
    #script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        if not row.isspace():
            print(BeautifulStrings(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    main()