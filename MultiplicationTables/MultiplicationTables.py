__author__ = 'Antimarvin'


def main():
    """
    Main execution
    """
    for i in range(1, 13):
        print formatList(genMultiList(i)).rstrip()


def genMultiList(multiplier):
    result = []
    for i in range(1, 13):
        result.append(i * multiplier)
    return result


def formatList(numbers):
    result = ''
    for num in numbers:
        numstr = ''
        for i in range(1, 5 - len(str(num))):
            numstr += ' '
        numstr += str(num)
        result += numstr
    return result


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert genMultiList(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "Failed 1"
    assert formatList([1, 2]) == '   1   2', "Failed formatting"
    main()
