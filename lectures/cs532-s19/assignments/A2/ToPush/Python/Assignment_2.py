import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import os
import jsonpickle
import requests
import json
from filterLinks import retrieveTweets
from filterLinks import deduplicateFunction
from filterLinks import genericErrorInfo
from filterLinks import extendURI
from filterLinks import filterLinksFunc
from filterLinks import removeDomain
from Mementos import getMemento
from CarbonDate import getCarbonDate

consumerKey = "C4ahlSSZeiKXVeBseLJTyJuiA"
consumerSecret = "XRTXkeKYlJt1D17PXWa9hXcJgKtBpUo9RDFCBeGqnsLnAweW2E"
accessToken = "1093707702033891329-XPvqu21IqAK6yJhTgm8e63X4ICJnfu"
accessSecret = "ToCPaNh7nr7dEJonE1OmNMsJqKRqaSA1RicLAxVoENTvU"


auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


allURI = []
extendedURI = []
removedTweetsURIs = []
filteredURIs = []

##################################################### USED EL CHAPO AND SHUTDOWN AND IMMIGRATION
#Maximum number of tweets we want to collect 
maxNumTweets = 2200

# The twitter Search API allows up to 100 tweets per query
tweetsCountMax = 100

numberTweets = 0
try:
	with open('LastPart.json', 'w') as myFile:
		for tweet in tweepy.Cursor(api.search, q="Immigration -filter:retweets",count = tweetsCountMax, include_entities=True).items(maxNumTweets):
				try:
					# if tweet.place is not None:
					myFile.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
					numberTweets += 1
					print (numberTweets)

				except:
					print("error")
		print("Retreived {0} Tweets".format(numberTweets))
except:
	print("error")
tweets = []


# ############## list that holds all URIs ###################
allURI = retrieveTweets()

# # # ############## list that holds extended URI ###############
extendedURI = extendURI(allURI)


# ############## list with removed twitter domain ###########
removedTweetsURIs = removeDomain(extendedURI)

# # ############## Completely filtered list ###################
filteredURIs = deduplicateFunction(removedTweetsURIs)


############# List to hold all URIs ##############
fullList = []

readFile = open("AllLinksOfficial.txt", "r")
	
###################### Had to strip lines because of formatting with newline #############	
for line in readFile:
	line = line.rstrip()
	fullList.append(line)
	


getMemento(fullList)

getCarbonDate(fullList)
