import importlib
import sys
from uriPlay import makeRequest
from filterTags import parseTags

#response = Server Response to request
response = makeRequest(sys.argv[1])

#links = links retrieved from user input URI
links = parseTags(response, sys.argv[1])

#list to hold uri of each pdf file
listPdfs = []

#loop through links and check if they are .pdf files
for link in links:
	try:
		responseObj = makeRequest(link)

		#check the response header for the correct content-type
		if("application/pdf" in (responseObj.headers.get('content-type'))):
			listPdfs.append(link);


	#general exception
	except Exception as e:
		print('error', str(e))

if(not listPdfs):
	print('No pdf files')

else:

	for pdf in listPdfs:
		res = makeRequest(pdf)
		print(("pdf URI: {0}, Status code: {1}, File Size:{2}").format(pdf, res.status_code, res.headers['content-length']))
