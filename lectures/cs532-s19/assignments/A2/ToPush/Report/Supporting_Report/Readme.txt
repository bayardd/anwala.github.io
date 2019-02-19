All of the URIs are in the Link_Tweets folder, in AllLinksOfficial.txt, the TweetTest2.json consists of Tweet objects that had URIs extracted from them.

The AllTimeMaps folder contains all of the TimeMaps gathered from MemGator. These files are recognized in the Time_Map_Related folder, which contains a 4 files. 

	Counter.txt contains the count of each Memento count of each URI, e.g. there was 876 URIs with 0 Mementos.
	ListNoMementos.json contains a list of the URIs that resulted in 0 Mementos.
	MementosTrack.json contains the URI, number of mementos, and the filename to which the URI corresponds.

The CarbonRecords.json folder contains all of the data gathered from the CarbonDating portion of the assignment. The numberCarbon.txt corresponds to the number of URIs that had a carbon date, (out of the total URI)

The Python file contains the Python files written to gather the data necessary for this assignment. 
	Assignment2.py is responsible for gathering Tweets and driving the program.
	filterLinks.py is responsible for filtering links, and writing the links to a file
	Mementos.py is responsible for collecting the TimeMap information, using the Docker image to gather data.
	CarbonDate.py does the same as Mementos.py but for the Carbon-Dates
	Histogram.py is responsible for reading the counts of each URI and Memento, (gathered earlier in the Counter.txt) and producing a histogram.
	ScatterPlot.py is responsible for reading the number of mementos from the MementosTrack, Carbon-Dates from the CarbonRecords (after finding matching URIs), and producing a dot plot.

	*** These files will not run correctly without the AllLinksOfficial.txt file. 

	The report folder contains everything used to render the Assignment_2.pdf. The graphs are included in the Figures directory.