from datetime import date
import json
import dateutil.parser
import matplotlib.pyplot as plt


xValues = []
yValues = []
allCarbon = []
allMemento = []
URIBoth = []
ageVsMemento = {"Age" : "value1", "MementoCount" : "value2"}
ageVsMementoList = []


mementoFile=open('MementosTrack.json')
carbonFile=open('CarbonRecords.json')


mementoData = json.load(mementoFile)
carbontoData = json.load(carbonFile)

#Used to calculate age of carbon-dates
today = (date.today())

#Get all URIs that have mementos
for i in range(0, 303):
	allMemento.append((mementoData[i]["URI"]))

#Get all URIs that have a carbon date
for x in range(0, 1179):
	allCarbon.append(carbontoData[x]["URI"])
	
#Contains list of URI that are similar to both
for URI in allMemento:
	if(URI in allCarbon):
		URIBoth.append(URI)
	
#Extract the Carbon date and Memento of each URI
for link in URIBoth:
	for a in carbontoData:
		if(a["URI"] == link and a["Carbon-Date"] != ""):
			
			toParse = a["Carbon-Date"]
			carbonDate = dateutil.parser.parse(toParse).date()

			age =  abs((today - carbonDate).days)


			ageVsMemento["Age"] = age

			
			for b in mementoData:
				if(b["URI"] == link):
					ageVsMemento["MementoCount"] = int(b["Mementos"])
					ageVsMementoList.append(ageVsMemento.copy())

for item in ageVsMementoList:
		xValues.append(item["Age"])
		yValues.append(item["MementoCount"])



#plot scatter plot based on the age and number of mementos
plt.ylim(0,1200)
plt.xlim(0,5000)
plt.scatter(xValues, yValues, alpha=0.5)
plt.title('URI Memento and Age Comparison')
plt.xlabel('Age (in days)')
plt.ylabel('Number of Mementos')

plt.show()



