__author__ = 'Antimarvin'

from sys import argv

def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def intersection(data):
    testlists = []
    lis = data.split(";")
    for li in lis:
        testlists.append(li.split(","))
    intersections = []
    for n in testlists[0]:
        if n in testlists[1]:
            intersections.append(n)
    result = ','.join(intersections)
    return result


def main():
    """
    Main execution
    """
    script, filename = argv
    #filename = 'testdata.txt'
    data = read_file_to_list(filename)

    for row in data:
        print(intersection(row.rstrip()))


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert intersection("1,2,3,4;4,5,6") == "4", "Failed Base"
    assert intersection("1,2,3,4; 5,6,7") == "", "Failed No intersection"
    assert intersection("1,2,3,4;3,4,5") == "3,4", "Failed multiple intersections"

    main()