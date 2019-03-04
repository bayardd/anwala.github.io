Notes:

The CalculationRecords.txt file contains all information on the TF, IDF, and TFIDF scores. The formatting appears correctly when the file maximized. I wanted to provide the entire URI, and if the display is not maximized the a few URIs will move to the next line.

The AllLinksOfficial.txt file contains all of the links which were used to download the HTML markup.

The Records.txt file contains the original URI, and the hashed filename that corresponds to that URI.

The FileOccurrance.txt is a simple use case. It was only used to store how many documents stored the query term.

The MatchedFormatted.json file contains all of the information regarding scanning the extracted text from the HTML files. It contains the URI, filename, query term, number of 
	words in the file, and occurrances of the query word in the file.

The selectedURIs file contains the 10 URIs that were selected to complete the assignment.



Python Files:

calculateStats.py is responsible for calculating the TF, IDF, and TFIDF. It formats the data, and outputs it to the CalculationRecords.txt file.

Driver.py is the main program. It calls each function responsible for completing the program.\

downloadHTML.py is responsible for making HTML requests to each of the URIs in AllOfficialLinks.txt, and downloading the HTML markup. It also creates hash codes for each of the
	files, and creates each of the files containing the HTML markup.

toText.py is responsible for extracting the text from the HTML files and creating new files with the extracted text.

searchText.py is responsible for searching the text for the query term and creating documentation on the searched files.




This selected link: https://www.nbcnews.com/politics/congress/government-shutdown-vote-border-bill-trump-n971576?cid=eml_nbn_20190214%0A,
actually produced an undefined error when searching for the page rank. An additional link was added to keep the count at 10.

All links were checked against https://www.prchecker.info/check_page_rank.php. All URIs that have a rating have been included in PageRanks.txt to be explicit. 
	An additional image called ProofPageRank.png has been added to show the formatting in the text editor.