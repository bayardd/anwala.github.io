import json
import requests
from filterLinks import genericErrorInfo
from collections import Counter

def getMemento(listURI):

	############ File which holds URIs with 0 Mementos ##################
	records = open("ListNoMementos.json", 'w')

	#################### File which holds all URI and their Memento Count #####################
	allMementos = open("MementosTrack.json", 'w')

	allMementosText = open("MementosTrackText.txt", 'w')

	#################### File which will hold occurrence of momento counts ###################
	amountEach = open("Count.txt", 'w')


	data = {"URI" : "value", "Mementos" : "value2"}
	dataGood = {"URI" : "value", "Mementos" : "value2", "TimeMapFileName" : "value3" }

	list = []
	total = {}
	counter = 0

	for URI in listURI:

		try:
			
			requestToMake = "http://localhost:5000/timemap/json/" + URI

			resp = requests.get(requestToMake, timeout=30)

			##Write response in json format ##
			json_obj = resp.json()


			try:

				counter += 1
				fileName = "TimeStamp" + str(counter) + ".json"

				file = open(fileName, 'w')

				json.dump(json_obj, file, indent=2)

				dataGood["URI"] = URI
				dataGood["Mementos"] = len(json_obj["mementos"]["list"])
				dataGood["TimeMapFileName"] = fileName

				allMementosText.write("URI: " + dataGood["URI"])
				allMementosText.write("\n")
				allMementosText.write("TimeMapFileName: " + dataGood["TimeMapFileName"])
				allMementosText.write("\n")
				allMementosText.write("Mementos: " + str(dataGood["Mementos"]))
				allMementosText.write("\n\n\n")

				json.dump(dataGood, allMementos, indent=2)

				list.append(len(json_obj["mementos"]["list"]))
				print("Added " + str(len(json_obj["mementos"]["list"])))
				
			except:
				print("Error Here")


		except:
			data["URI"] = URI
			data["Mementos"] = 0
		
			json.dump(data, records, indent = 2)

			print("Added 0 Mementos")
			list.append(0)

	amountEach.write(str((Counter(list))))
