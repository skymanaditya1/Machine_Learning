'''This is a simple implementation of the Naive Bayes Algorithm
'''

import csv
import numpy
import operator

if __name__=="__main__":

	with open('nbdata.csv', 'rb') as dataFile:
		reader = csv.reader(dataFile)
		data = list(reader)
	# print(data)

	class_frequency = {}
	class_count = {}
	# Generate a count of all the class values

	for class_value in data:
		if class_value[-1] in class_count:
			class_count[class_value[-1]] += 1
		else:
			class_count[class_value[-1]] = 1.0
	print(class_count)

	# Compute the class probabilities
	for class_value in class_count:
		class_frequency[class_value] = class_count[class_value] / len(data)

	print(class_frequency)


	# A test example
	test_data = ['Sunny', 'Cool', 'High', 'Strong']

	class_likelihood = {}
	class_attribute_count = {}
	# Compute the likelihood for all the target_values
	for class_value in class_frequency:
		class_likelihood[class_value] = 1 # Assign initial probability
		attribute_count = {}
		list = []
		for d in data:
			if d[-1] == class_value:
				for i in range(len(test_data)):
					if d[i + 1] == test_data[i]:
						if d[i+1] in attribute_count:
							attribute_count[d[i+1]] += 1
						else:
							attribute_count[d[i+1]] = 1.0
		class_likelihood[class_value] *= class_frequency[class_value]
		for i in attribute_count:
			class_likelihood[class_value] *= attribute_count[i] / class_count[class_value]

	
	print("The class probability distribution is : ")
	print(class_likelihood)

	total = 0.0
	for val in class_likelihood:
		total += class_likelihood[val]
	conditional_probability = {}
	for class_value in class_likelihood:
		conditional_probability[class_value] = class_likelihood[class_value] / total
	
	print("The conditional probability distributions are : ")
	print(conditional_probability)

	max_value = 0.0
	target_value = None
	for prob_value in conditional_probability:
		if conditional_probability[prob_value] > max_value:
			max_value = conditional_probability[prob_value]
			target_value = prob_value

	print("The target function output is : " + target_value)