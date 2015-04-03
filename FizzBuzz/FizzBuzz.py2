from sys import argv

def get_data_sets(filename):
	"""
	Gets a list of lists with the lists containing ints from a file
	with lines containing 3 ints separated by spaces
	"""
	with open(filename) as f:
		content = f.readlines()
	return formatted_datasets(content)

def formatted_datasets(content):
	"""
	Takes a list of strings, splits each string on spaces and converts
	to ints. Returns a list of lists containing the ints.
	"""
	list_of_lists = []
	for i in content:
		temp_list = [int(x) for x in i.split()]
		list_of_lists.append(temp_list)
	return list_of_lists

def fizzbuzz(arguments):
	"""
	Takes a list containing the three parameters (first_div, Second Div, Length)
	and uses this to return a string that replaces the values that divide
	evenly by the divs with an F, B, or FB if both. I.E.

	[2,7,15] == "1 F 3 F 5 F B F 9 F 11 F 13 FB 15"
	"""
	first_div, second_div, length = arguments
	result = ""
	for i in range(1,length+1):
		if (i % first_div == 0 and i % second_div == 0):
			result +="FB "
		elif i % first_div == 0:
			result += "F "
		elif i % second_div == 0:
			result += "B "
		else:
			result += str(i) + " "
	return result[:-1] #remove the trailing space

def main():
	"""
	Main execution
	"""
	script, filename = argv

	data = get_data_sets(filename)

	for data_point in data:
		print fizzbuzz(data_point)

if __name__ == '__main__':
	"""
	Runs only if file is run directly and contains self evaluating asserts
	"""
	assert formatted_datasets(["1 2 5", "2 4 6"]) == [[1,2,5], [2,4,6]], "Failed formatted_datasets"
	assert fizzbuzz([3,5,10]) == "1 2 F 4 B F 7 8 F B", "Failed Simple 3,5,10 fizzbuzz"
	assert fizzbuzz([2,7,15]) == "1 F 3 F 5 F B F 9 F 11 F 13 FB 15", "Failed 2,7,15 fizzbuzz"
	main()