import requests
import hashlib
import pickle
import json

def downloadMarkup():
	fullList = []
	fullRecords = []
	

	readFile = open("AllLinksOfficial.txt", "r")
	tempFile = open("tempFile.txt", 'w')
	
	###################### Had to strip lines because of formatting with newline #############	
	for line in readFile:
		line = line.rstrip()
		fullList.append(line)

	i = 0

	for URI in fullList:
		i = i+1
		print(i)
		uri = URI.strip()
		if(len(uri) == 0):
			print("Empty")

		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
				'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Connection' : 'keep-alive',
				'Cache-Control' : 'max-age=0'}

		try:
			response = requests.get(uri, allow_redirects=True, timeout=30)

		except Exception as e:
			print('Error: ', str(e))

		tempFile.write(response.text)
		

		hasher = hashlib.md5()

		with open('tempFile.txt', 'rb') as afile:
   			buf = afile.read()
   			hasher.update(buf)
   			
		# print(hasher.hexdigest())

		fileName = hasher.hexdigest() + '.html'

		#Write to the specified file (with hash code)
		writeComplete = open(fileName, 'w')

		writeComplete.write(response.text)

		fullRecords.append({'URI' : URI, 'FileName' : fileName})

	with open('Records.txt', 'w') as record:
		record.write(json.dumps(fullRecords, indent=2))

	### Encode fill will not be readable
	with open('JSONRecords.json', 'wb') as file:
		pickle.dump(fullRecords, file, protocol=pickle.HIGHEST_PROTOCOL)




	#Used to read file
	# with open('fileRecords.json', 'rb') as fp:
	# 	data = pickle.load(fp)

	# for a in data:
	# 	print(a['URI'])   			


