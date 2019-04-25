from googlesearch import search
import csv
import urllib.parse
import requests
import feedparser
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlparse
import re
import clusters
import sys


RSSURLs = []
fileURL = []
feedList = []
listURLs = []
listSplit = []
top1000 = []
domains = {'blogspot.com'}
dataFile = open("blogdata.txt", 'w')
centralFile = open("clusteredBlogsExtra.txt", 'w')


# for url in search( query="music", stop=170, domains = domains):

# 	splitURL = urlparse(url)

# 	# if list is not empty
# 	if((not listURLs) == False):

# 		for domain in listURLs:
# 			splitDomain = urlparse(domain)

# 			listSplit.append(splitDomain.netloc.split('.')[0])

# 		if(splitURL.netloc.split('.')[0] not in listSplit):
# 			listURLs.append(url)
# 			print(url)

# 	else:
# 		listURLs.append(url)
	


# with open('UrlCollection.csv', mode='w') as URIs:
#     write = csv.writer(URIs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     for url in listURLs:
#     	write.writerow([url])
    


# with open('UrlCollection.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         for key, value in row.items():
#         	fileURL.append(value)

# f = open("MusicURLs.txt", 'r')
# lines=[line for line in f]

# for line in lines:
#     fileURL.append(line)



def findfeed(site):
    try:
        raw = requests.get(site).text
    except:
        print("error")
        raw = ""
    result = []
    possible_feeds = []
    html = bs4(raw)
    feed_urls = html.findAll("link", rel="alternate")
    for f in feed_urls:
        t = f.get("type",None)
        if t:
            if "rss" in t or "xml" in t:
                href = f.get("href",None)
                if href:
                    possible_feeds.append(href)
    parsed_url = urllib.parse.urlparse(site)
    base = parsed_url.scheme+"://"+parsed_url.hostname
    atags = html.findAll("a")
    for a in atags:
        href = a.get("href",None)
        if href:
            if "xml" in href or "rss" in href or "feed" in href:
                possible_feeds.append(base+href)
    for url in list(set(possible_feeds)):
        f = feedparser.parse(url)
        if len(f.entries) > 0:
            if url not in result:
                result.append(url)

    return(result)


# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
 # Parse the feed
	d=feedparser.parse(url)
	wc={}
 	# Loop over all the entries
	for e in d.entries:

 		# Extract a list of words
		words=getwords(e.title)

		for word in words:
			wc.setdefault(word,0)
			wc[word]+=1

	return d.feed.title,wc



def getwords(html):

	 # Remove all the HTML tags
	txt=re.compile(r'<[^>]+>').sub('',html)
	
	# Split words by all non-alpha characters
	words=re.compile(r'[^A-Z^a-z]+').split(txt)
 
 	# Convert to lowercase
	return [word.lower( ) for word in words if word!='']


# for url in fileURL:
# 	result = findfeed(url)
# 	print(result)

# 	if(not result == False):
# 		try:
# 			RSSURLs.append(result[0])
# 		except:
# 			print("error")



# with open('RSSExtraCollection.csv', mode='w') as URIs:
#     write = csv.writer(URIs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     for url in RSSURLs:
#     	write.writerow([url])



with open('RSSExtraCollection.csv', mode='r') as test:
	
	reader = csv.DictReader(test)

	for row in reader:

		for key, value in row.items():
			print(value)
			feedList.append(value)


apcount = {}
wordcounts = {}
for feedurl in feedList:
	try:
		(title, wc) = getwordcounts(feedurl)
		wordcounts[title] = wc
		for (word, count) in wc.items():
			apcount.setdefault(word, 0)

			if count > 1:
				apcount[word] += 1
	except:
		print ('Failed to parse feed %s' % feedurl)
count2 = 0
wordlist = []
for (w, bc) in apcount.items():
    frac = float(bc) / len(feedList)

    if(frac > .001 and frac < .8 and len(wordlist) < 1000):
        count2 += 1
        print(count2)
        wordlist.append(w)

dataFile.write('Blog')
for word in wordlist: dataFile.write('\t%s' % word)
dataFile.write('\n')
for (blog, wc) in wordcounts.items():
    dataFile.write(blog)

    for word in wordlist:
        if word in wc:
            dataFile.write('\t%d' % wc[word])
        else:
            dataFile.write('\t0')
    dataFile.write('\n')


dataFile.close()

blognames,words,data=clusters.readfile('blogdata.txt')
clust=clusters.hcluster(data)
asciiFile = open("ascii2.txt", 'w') 
orig_stdout = sys.stdout
sys.stdout = asciiFile

clusters.printclust(clust,labels=blognames)

sys.stdout = orig_stdout

asciiFile.close()

clusters.drawdendrogram(clust,blognames,jpeg='blogclustExtra.jpg') 

kclust=clusters.kcluster(data,k=5)
centralFile.write('K = 5' + '\n')
centralFile.write("Number of Iterations: 5" + '\n')

for x in range(0,5):

	for r in kclust[x]:
		centralFile.write(blognames[r] + '\n')
		centralFile.write('\n')
	centralFile.write('\n')
	centralFile.write("-------------------------------------------")
	centralFile.write('\n')


kclust=clusters.kcluster(data,k=10)
centralFile.write('\n')
centralFile.write('K = 10' + '\n')
centralFile.write("Number of Iterations: 5" + '\n')

for y in range(0,10):
	for r in kclust[y]:
		centralFile.write(blognames[r] + '\n')
	centralFile.write('\n')
	centralFile.write("-------------------------------------------")
	centralFile.write('\n')


centralFile.write('\n')
kclust=clusters.kcluster(data,k=20)
centralFile.write('K = 20' + '\n')
centralFile.write("Number of Iterations: 3" + '\n')

for z in range(0,20):
	for r in kclust[z]:
		centralFile.write(blognames[r] + '\n')
	centralFile.write('\n')	
	centralFile.write("------------------------------------------")
	centralFile.write('\n')

coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2dExtra.jpg')