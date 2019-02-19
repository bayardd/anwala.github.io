import requests
import os, sys
import json
from urllib.parse import urlparse


################### Rename....
def retrieveTweets():

	tweets = []
	listURI = []

	for line in open('LastPart2.json', 'r'):
		tweets.append(json.loads(line))
		

	for tweet in tweets:
		for shortUri in (tweet['entities']['urls']):
			listURI.append((shortUri['expanded_url']))

	return listURI




def deduplicateFunction(unsanitizedList):

	deduplicatedList = []

	try:
		
		for URI in unsanitizedList:
			scheme, netloc, path, params, query, fragment = urlparse(URI)
			toCheck = netloc + path

		
			if toCheck not in deduplicatedList:
  				deduplicatedList.append(URI)
	except:
		genericErrorInfo()

	return set(deduplicatedList)

############################## Move to testing file #############################################
def genericErrorInfo():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
	print('\tERROR:', errorMessage)




####################### Takes List of URI and extends them, also grabs status code ######################
def extendURI(allURI):
	i = 0

	newList = []
	for URL in allURI:
		
		try:
			link, statusCode = filterLinksFunc(URL)

			if(statusCode == 200):
				newList.append(link)

			else:
				counter = 0;
				while(statusCode != 200 and counter != 5):
					filterLinksFunc(link)
					counter = counter + 1

		except:
			genericErrorInfo()


	return newList


############################## Extends the links #####################################

def filterLinksFunc(URI):

	
	try:
		resp = requests.head(URI, allow_redirects=True, timeout = 2)

	except:
		genericErrorInfo()
	return resp.url, resp.status_code



################################ Remove links with Twitter Domain #########################
def removeDomain(allURI):

	count = 0
	newList = []

	for URI in allURI:
		scheme, netloc, path, params, query, fragment = urlparse(URI)

		try:	

			if(netloc != "twitter.com"):
				newList.append(URI)
				
				# print("link from twitter..")

		except:
			genericErrorInfo()

	return newList

