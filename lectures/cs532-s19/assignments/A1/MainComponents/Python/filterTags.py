from bs4 import BeautifulSoup
from urllib.parse import urlparse


def parseTags(response, uri):

	#break uri into seperate components
	scheme, netloc, path, params, query, fragment = urlparse(uri)
	mainPage = scheme + "://" + netloc

	#dereference the response object
	redditHtml = response.text

	listLinks = []

	#Parse the document and retrieve all <a> tags
	soup = BeautifulSoup(redditHtml, "html.parser")
	for links in soup.find_all('a'):

		#Retrieve the link from the a tag
		x = links.get('href')

		#Make sure the link is not empty
		if(x == None):
			continue

		#In case we deal with a relative path
		try:
			if(not x.strip().startswith('http')):
			#if input is relative path, append scheme and netloc to beginning
				x = mainPage + x

			#will produce a list full of href links
			listLinks.append(x)

		except Exception as e:
			print("Error", str(e))

	return listLinks