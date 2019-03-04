import pickle
import os
import json
from operator import itemgetter
import scipy as sp
import scipy.stats


def calculateStats():
	#will be used to enter page ranks and normalize them
	## had to put 0 for undefind URL (Will be noted in Readme and Report)
	listURI = [
	"https://www.cnn.com/2019/02/14/politics/national-emergency-immigration/index.html", 
	"https://www.vox.com/policy-and-politics/2019/1/8/18172749/trump-national-emergency-government-shutdown-wall",
	"https://apnews.com/18b632a262634e31918344f2c74a8e32",
	"https://newspunch.com/trump-sign-executive-order-extra-wall-funds-avoid-shutdown/",
	"https://www.reuters.com/article/us-usa-shutdown/u-s-congress-poised-to-vote-on-border-measure-without-trump-wall-idUSKCN1Q30KU?feedType=RSS&feedName=topNews%0A",
	"https://fullmagazine.us/immigration-spending-pact-has-more-than-a-border-wall/",
	"https://dailywn.com/news/224240%0A",
	"https://in.reuters.com/article/usa-shutdown/trump-to-sign-border-bill-declare-emergency-seeking-wall-funds-idINKCN1Q30M6?feedType=RSS&feedName=topNews%0A",
	"http://www.msn.com/en-us/news/opinion/republicans-are-stuck-with-a-lousy-deal/ar-BBTw9kr?ocid=st%0A",
	"https://whyy.org/npr_story_post/trump-will-sign-border-compromise-to-avert-shutdown-along-with-emergency-declaration/",
	"https://www.nytimes.com/2019/02/14/us/politics/congress-trump-border-deal-wall.html?smid=nytcore-ios-share%0A",
	"https://www.theguardian.com/us-news/live/2019/feb/14/trump-news-live-government-shutdown-deal-latest-updates-democrats-republicans-us-politics-today?CMP=edit_2221%0A",
	"https://www.facebook.com/142474049098533/posts/2349521521727097?sfns=mo%0A",
	"https://www.upi.com/Top_News/US/2019/02/14/Lawmakers-submit-bipartisan-bill-to-avoid-second-shutdown/4671550133911/?spt=su&or=btn_tw%0A",
	"https://www.numbersusa.com/news/numbersusa-opposes-budget-deal-advocates-continuing-resolution",
	"https://www.cnbc.com/2019/02/14/trump-decides-whether-to-sign-border-security-deal-to-avoid-shutdown.html?__source=facebook%7Cmain&fbclid=IwAR1eLYZjWdA6",
	"https://www.nbcnews.com/politics/congress/government-shutdown-vote-border-bill-trump-n971576?cid=eml_nbn_20190214%0A"
	]

	listRanks = [9,6,0,0,8,0,0,8,8,6,0,7,9,7,6,7,0]
	normalizedRanks = []


	## Initialize for use in function
	collectionCalc = []
	collectionURI = []
	collectionTFIDF = []
	# collectionTF = []
	# collectionIDF = []

	## Open Files
	recordsFile = open("CalculationRecords2.txt", "w")
	pageRankFile = open("PageRanks.txt", "w")
	failedRanks = open("NoRanks.txt", "w")
	correlationFile = open("Correlation.txt", "w")

	## Formatting Output
	alreadySet = False
	titleSet = False
	tab = ('\t')
	newline = ('\n') 

	#Get total count for use in formula
	with open("fileOccurrance.txt") as toRead:
		totalCount = toRead.readline()
		
	totalCount = int(totalCount)

	# Get URIs for 10 files that are being used #
	with open("selectedURIs.txt") as readURI:
		for line in readURI: 
			URI = readURI.readline()
			strippedURI = URI.rstrip()
			collectionURI.append(strippedURI)

	
	## Unload data file ##
	with open('RecordsJson.json', 'rb') as fp:
		data = pickle.load(fp)

	for entry in data:
		checkURI = entry["URI"]
		calcData = {'TFDIF' : 'val1', 'TF' : 'val2', 'IDF' : 'val3', 'URI' : 'val3'}
		if(checkURI in collectionURI):
			## Word Count (Frequency) / Number of words found in document
			TF = entry["WordCount"] / entry["NumberWords"]
			roundedTF = round(TF,4)

			## Had a total of 1130 documents, Word was found in 375 documents out of 1130
			IDF = 1130/375
			roundedIDF = round(IDF,4)
			
			TF_IDF = TF * IDF
			roundedTF_IDF = round(TF_IDF, 4)

			calcData["TFDIF"] = roundedTF_IDF
			calcData["TF"] = roundedTF
			calcData["IDF"] = roundedIDF
			calcData["URI"] = entry["URI"]

			collectionCalc.append(calcData)
			# collectionTF.append(roundedTF)
			collectionTFIDF.append(roundedTF_IDF)
			# collectionIDF.append(roundedIDF)
	
	maxRank = max(listRanks)
	minRank = min(listRanks)
	
	# Normalize Page Ranks #
	for rank in listRanks:
		normalized = (int(rank)- int(minRank))/(maxRank - minRank)
		roundedNormalized = round(normalized,1)
		normalizedRanks.append(roundedNormalized)


	## Used to create association between URI and Rank
	pageRanks = dict( zip(listURI,normalizedRanks ))


	# Sort Records #
	newlist = sorted(collectionCalc, key=itemgetter('TFDIF'), reverse=True)
	sortedRanks = sorted(pageRanks.items(), key=itemgetter(1), reverse=True)


	# Formatting For Page Ranks # 
	titleRank = (f"Page Rank {tab} URI {newline}")
	underscoreRank = f"---------- {tab} ---{newline}"

	for key, value in sortedRanks:

		formattedOutput = f"{value} {tab}{tab} {key} {tab}{newline}"

		if(titleSet != True):
			pageRankFile.write(titleRank)
			pageRankFile.write(underscoreRank)
			failedRanks.write(titleRank)
			failedRanks.write(underscoreRank)
			titleSet = True;

		if(value != 0):
			pageRankFile.write(formattedOutput)

		else:
			failedRanks.write(formattedOutput)




	# Formatting For TFDIF TF and IDF #
	title = (f"TFIDF {tab} TF {tab} IDF {tab} URI {newline}")
	underscore = f"----- {tab} -- {tab} --- {tab} --- {newline}"

	for iteration in newlist:

		formattedScores = f"{iteration['TFDIF']:.4f} {tab} {iteration['TF']:.4f}  {iteration['IDF']:.4f}  {iteration['URI']}{newline}"

		if(alreadySet != True):
			recordsFile.write(title)
			recordsFile.write(underscore)
			# recordsFile.write('%-10s %6s %10s %2s\n' % ("TFIDF", "TF", "IDF", "URI"))
			alreadySet = True

		recordsFile.write(formattedScores)


	## Calculate Kendall Tau_b Score TFIDF ##
	tauTFIDF, p_valueTFIDF = sp.stats.kendalltau(normalizedRanks, collectionTFIDF)

	## Calculate Kendall Tau_b Score TF ##
	# tauTF, p_valueTF = sp.stats.kendalltau(normalizedRanks, collectionTF)

	## Calculate Kendall Tau_b Score IDF ##
	
	# Round Value #
	roundedTFIDF = round(tauTFIDF,2)
	roundedTFIDF_P = round(p_valueTFIDF,2)
	# roundedTF = round(tauTF,2)
	# roundedTF_P = round(p_valueTF,2)

	rowTFIDF_Tau = (f"TFIDF VS Page Rank Tau_b {tab} {roundedTFIDF}{newline}")
	rowTFIDF_P = (f"TFIDF VS Page Rank p val. {tab} {roundedTFIDF_P}{newline}")
	# rowTF_Tau = (f"TF VS Page Rank Tau_b {tab} {roundedTF}{newline}")
	# rowTF_P = (f"TF VS Page Rank Tau_b {tab} {roundedTF_P}{newline}")
	# rowIDF_Tau = (f"IDF VS Page Rank Tau_b {tab} {tauIDF} {newline}")
	# rowIDF_P = (f"IDF VS Page Rank p val. {tab} {p_valueIDF}{newline}")
	
	correlationFile.write(rowTFIDF_Tau)
	correlationFile.write(rowTFIDF_P)
	# correlationFile.write(rowTF_Tau)
	# correlationFile.write(rowTF_P)
	# correlationFile.write(rowIDF_Tau)
	# correlationFile.write(rowIDF_P)

	# print(roundedTFIDF)
	# print(roundedTFIDF_P)
	# print(roundedTF)
	# print(roundedTF_P)
	