import requests
import json
from filterLinks import genericErrorInfo
import pickle

def getCarbonDate(listURI):
	numberCarbonDates = 0	
	carbonRecords = open("CarbonRecords.json", 'w')
	numberCarbonFile = open("numberCarbon.txt", 'w')
	
	dictFormat = {"URI" : "key", "Carbon-Date" : "key"}
	i = 0
	

	for URI in listURI:

		try:
			# data = {'URI' : URI, "Carbon-Date" : carbonDate}

			requestToMake = "http://localhost:8888/cd/" + URI
			resp = requests.get(requestToMake)



		except:
			print(genericErrorInfo)

		try:
			json_obj = resp.json()

		except:
			print(genericErrorInfo())

		# total['URI'] = URI

		try:
			json_obj = json.loads(resp.text)

			i = i+1
			print(i)

			dictFormat["URI"] = (json_obj["uri"])
			dictFormat["Carbon-Date"] = (json_obj["estimated-creation-date"])

			if(json_obj['estimated-creation-date'] != ""):
				numberCarbonDates += 1
		
			with open('test.json', 'w') as f:
				pickle.dump(dictFormat, f, protocol=pickle.HIGHEST_PROTOCOL)
				
		except:
			print(genericErrorInfo())

	numberCarbonFile.write(str(numberCarbonDates))

		