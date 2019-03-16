import csv
import json
import pickle

def readCSV():
    friendsValues = []
    orderedFriends = {"Friend" : "value1", "Number_Friends" : "value2"}
    
    with open('acnwala-friendscount.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            #Not adding column names to dictionary
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            ## Add all values to dictionary from .csv file
            else:
                orderedFriends["Friend"] = row[0]
                orderedFriends["Number_Friends"] = row[1]
                toAppend = orderedFriends.copy()
                friendsValues.append(toAppend);
                line_count += 1

    return friendsValues

def readJSON():
    followers = []

    with open('EncodedFollowersExtraCredit.json', 'rb') as fp:
        data = pickle.load(fp)
        
    return data
