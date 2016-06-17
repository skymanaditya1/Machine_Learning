'''Program to count the number of distinct words in a given file'''
if __name__ == "__main__":
	with open('txt', 'r') as reader:
		data = reader.read().replace('\n', ' ').split()
	# Dictionary, key => word, value => number of occurrence in the file
	dic = {}
	for word in data:
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	print(dic)