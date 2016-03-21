__author__ = 'Antimarvin'

from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def main():
    """
    Main execution
    """
    script, filename = argv

    for line in read_file_to_list(filename):
        print line.lower().replace("\n", "")  # had to remove new lines


if __name__ == '__main__':

    main()
