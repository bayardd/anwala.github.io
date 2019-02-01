import requests


def makeRequest(uri):
	
	uri = uri.strip()
	if(len(uri) == 0):
		return ''

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
				'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Connection' : 'keep-alive',
				'Cache-Control' : 'max-age=0'}

	try:
		response = requests.get(uri, headers = headers, timeout=10)

	except Exception as e:
		print('Error: ', str(e))

	return response




