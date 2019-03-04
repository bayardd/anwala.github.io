import subprocess
import pickle
import os
import json
from collections import Counter

def grep():
	arg = "Congress"
	records = []
	URIs = []

	## Unload Data File##
	with open('JSONRecords.json', 'rb') as fp:
		data = pickle.load(fp)

	#Simple text file to hold number of files that match word
	fileOccurrance = open("fileOccurrance.txt" , 'w')

	#Used to keep track of how many files contain the word
	fileCounter = 0

	#loop through all html files
	for a in data:

		fileName, file_extension = os.path.splitext(a['FileName'])

		#convert filename to text file
		completeName = "./ExtractedText/" + fileName + ".txt"

		process = subprocess.Popen(['grep', '-rwn', arg, completeName], stdout=subprocess.PIPE)
		stdout, stderr = process.communicate()
		if len(stdout) != 0:
			num_words = 0

			with open(completeName, 'r') as readFile:
				for line in readFile:
					words = line.split()

					## Keeps track of number of words in file ##
					num_words += len(words)
				

			with open(completeName) as toCount:

				## Code from Joshua on slack, Counts occurrance of query term in document##
				wordcount = Counter(toCount.read().split()) 
				wordOuccurance = wordcount['Congress']

				if(wordOuccurance != 0): 
					fileCounter += 1
					# print(fileCounter)

			data = {"URI" : a['URI'], "FileName" : a['FileName'], "Word" : arg, "NumberWords" : num_words, "WordCount" : wordOuccurance}
			records.append(data)


			with open('MatchedFormatted.json', 'w') as record:
				record.write(json.dumps(records, indent=2))

			#### File contains all records with URI, Filename, query word, and number of words found per file
			with open('RecordsJson.json', 'wb') as file:
				pickle.dump(records, file, protocol=pickle.HIGHEST_PROTOCOL)

			URIs.append(a['URI'])

	# Writes total number of files with "Congress" to file for later calculations
	fileOccurrance.write(str(fileCounter))