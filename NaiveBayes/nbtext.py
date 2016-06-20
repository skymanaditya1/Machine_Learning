'''Sentiment Analysis on twitter feeds using Naive Bayes Classifier'''
import numpy
import csv

def naive_bayes():
	# Step 1:
	# |vocabulary| - number of distinct words found within the training data
	vocabulary = []
	with open('nbtextdata.csv', 'r') as reader:
		words = reader.read().replace(',', ' ').replace('.', '').split()

	word_count = 0.0 # Count of total words in the training data
	for word in words:
		word_count += 1
		if word not in vocabulary:
			vocabulary.append(word)
	
	print(word_count)
	print(len(vocabulary))

	train_words = {}
	for line in data:
		words = line[0].replace(',', ' ').replace('.', '').split()
		for word in words:
			if word.lower() in train_words:
				train_words[word.lower()] += 1
			else:
				train_words[word.lower()] = 1.0

	#print(train_words)


	# Step 2:
	# Calculate the class probability distributions P(Vj) and P(Wk|Vj)
	class_count = {}
	class_frequency = {}

	for line in data:
		if line[1] in class_count:
			class_count[line[1]] += 1
		else:
			class_count[line[1]] = 1.0

	for class_value in class_count:
		class_frequency[class_value] = class_count[class_value] / len(data)


	#print(class_frequency)
	#print(class_count)

	class_likelihood = {}
	
	test_data = "Party have a meeting tomorrow at the university"
	test_words = test_data.replace(',', ' ').replace('.', ' ').lower().split()
	# print(test_words)

	for class_value in class_count:
		class_attribute_count = {}
		class_likelihood[class_value] = class_frequency[class_value] # Assigns initial prob.
		for line in data:
			# print(line)
			if line[-1] == class_value:
				line_words = line[0].replace(',', ' ').replace('.', ' ').lower().split()
				# print(line_words)
				for test_word in test_words:
					# print(test_word)
					if test_word in line_words:
						# print("Word " + test_word + " found in line_words")
						if test_word in class_attribute_count:
							# print("Word " + test_word + " found in dictionary")
							class_attribute_count[test_word] += 1
						else:
							# print("Word " + test_word + " found for the first time")	
							class_attribute_count[test_word] = 1.0
					# else:
						# class_attribute_count[test_word] = 0.0

		for test_word in test_words:
			if test_word not in class_attribute_count:
				class_attribute_count[test_word] = 0.0
		print(class_attribute_count)

		for i in class_attribute_count:
			class_likelihood[class_value] *= (class_attribute_count[i] + 1) / (len(vocabulary) + word_count) 
		print(class_likelihood)

	
	# Compute the likelihood for all the target values
	class_distribution = {}
	class_target = None
	maxVal = 0
	total_target = 0.0
	for target_value in class_likelihood:
		total_target += class_likelihood[target_value]

	print(total_target)

	for target_value in class_likelihood:
		class_distribution[target_value] = class_likelihood[target_value] / total_target
		if class_distribution[target_value] > maxVal:
			maxVal = class_distribution[target_value]
			class_target = target_value			

	print(class_distribution)
	print("The target is : " + class_target)


	# print("Hello")
	# Step 3:
	# Calculate the Bayesian probabilites using Naive Bayes classifier 


if __name__ == "__main__":
	with open('nbtextdata.csv', 'rb') as dataFile:
		reader = csv.reader(dataFile)
		data = list(reader)
	naive_bayes()