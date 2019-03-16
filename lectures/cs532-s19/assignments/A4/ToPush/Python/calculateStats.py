import statistics
import csv
def extractList(listValues):

    listNumbers = []

    for friendCount in listValues:
        listNumbers.append(int(friendCount["Number_Friends"]))
    print(listNumbers)
    return listNumbers

def extractSerialized(listValues):

    listNumbers = []

    for value in listValues:
        listNumbers.append(value['Number_Following'])

    return listNumbers


def userFriendCountFacebook(listValues):
    print("Prof. Nwalas Friends Facebook" + '\t' + str(len(listValues)))
    return len(listValues)

def userFriendCountTwitter(listValues):

    with open('FollowerRecordsExtraCredit.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 1
        for row in csv_reader:

            if(line_count == 2):
                numberFriends = row[1]

                line_count += 1

                print("Prof. Nwalas Friends Twitter" + '\t' + str(numberFriends))
                return numberFriends
            else:
                line_count += 1

def calculateMean(listValues):

    average = statistics.mean(listValues)
    roundedAverage = round(average,2)

    print("Average" + '\t' +  str(roundedAverage))
    return roundedAverage


def calculateMedian(listValues):

    median = statistics.median(listValues)

    print("Median" +'\t'+ str(median))
    return median

def calculateSdv(listValues):

    SD = statistics.stdev(listValues)
    roundedSD = round(SD,2)

    print("SD" +'\t'+ str(roundedSD))
    return roundedSD
