__author__ = 'Antimarvin'
from sys import argv



def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def create_database(height, width):
    database=[[0 for j in range(width)] for i in range(width)]
    return database



def set_values(data, type, index, value):
    if type == 'Col':
        for row in data:
            row[index] = value
    elif type == 'Row':
        for col in range(len(data[index])):
            data[index][col] = value
    else:
        assert TypeError
    return data


def query(data, type, index):
    if type == 'Col':
        result=0
        for row in data:
            result += row[index]
        return result
    elif type == 'Row':
        return sum(data[index])

def main():
    """
    Main execution
    """
    #script, filename = argv
    filename = 'testdata.txt'
    data = read_file_to_list(filename)

    database = create_database(256, 256)

    for row in data:
        if not row.isspace():
            row = row.rstrip()
            command = row.split(' ')
            if command[0] == 'SetCol':
                database = set_values(database, 'Col', int(command[1]), int(command[2]))
            elif command[0] == 'SetRow':
                database = set_values(database, 'Row', int(command[1]), int(command[2]))
            elif command[0] == 'QueryCol':
                print(query(database, 'Col', int(command[1])))
            elif command[0] == 'QueryRow':
                print(query(database, 'Row', int(command[1])))
            else:
                print('Not a valid Command')

if __name__ == '__main__':
    """
    Runs only if file is run directly and contains self evaluating asserts
    """
    main()