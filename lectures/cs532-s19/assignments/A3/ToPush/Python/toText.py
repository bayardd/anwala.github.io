import pickle
import os
from boilerpipe.extract import Extractor
import numpy

def convertToText():
	html = []

	# Used to read file
	with open('JSONRecords.json', 'rb') as fp:
		data = pickle.load(fp)

	#loop through all html files
	for a in data:
		# print(a['FileName'])

		with open(a['FileName'] , 'r') as read:
			html = read.read()

		#Extract html from file
		extractor = Extractor(extractor='ArticleExtractor', html=html)
		extractedText = extractor.getText()

		# print(extractedText)

		#split text to identify filename 
		fileName, file_extension = os.path.splitext(a['FileName'])

		# print(fileName)

		#convert filename to text file
		completeName = fileName + ".txt"

		path = os.path.join(os.path.expanduser('~'),'Documents/CS532/CS532_Assignment3/Assignment3/Files3/ExtractedText/',completeName)

		# print(path)

		#write extracted text to new file
		with open(path, 'w') as file:
			file.write(extractedText)



		# print(a['FileName'])   			
