__author__ = 'Antimarvin'

from sys import argv


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


def reversed_sentence(sentence):
    result = ''
    for word in sentence.split()[::-1]:
        result += word + ' '
    return result[:-1]  # remove trailing space


def main():
    """
    Main execution
    """
    script, filename = argv

    sentences = read_file_to_list(filename)

    for sentence in sentences:
        print reversed_sentence(sentence)


if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    assert reversed_sentence("Hello World") == "World Hello", "Failed 2 word Sentence"
    assert reversed_sentence("Hello Big World") == "World Big Hello", "Failed 3 word Sentence"
    assert reversed_sentence("Hello Great Big World") == "World Big Great Hello", "Failed 4 word Sentence"
    main()