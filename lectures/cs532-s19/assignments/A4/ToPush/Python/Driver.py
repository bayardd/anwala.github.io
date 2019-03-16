import readFiles
import calculateStats
import createGraph
import extractFollowers

# ID to use for Twitter
ID = "acnwala"

## Holds numbers of friends for Facebook
extractedNumbersFacebook = []

## Holds number of friends for Twitter
extractedNumbersTwitter = []

## Reads File
# listValues = readFiles.readCSV()

## Extracts numbers from friends list
# extractedNumbersFacebook = calculateStats.extractList(listValues)

## Prof, Nwalas Friend Count FaceBook
# personalCountFacebook = calculateStats.userFriendCountFacebook(extractedNumbersFacebook)

## Calculate Mean
# meanFacebook = calculateStats.calculateMean(extractedNumbersFacebook)

## Calculate Median
# medianFacebook = calculateStats.calculateMedian(extractedNumbersFacebook)

##Calculate Stand Deviation
# standardDevFacebook = calculateStats.calculateSdv(extractedNumbersFacebook)

## Create First Graph
# createGraph.CumulativeGraph(extractedNumbersFacebook, personalCountFacebook, meanFacebook, medianFacebook, standardDevFacebook)

## Extract Followers from Twitter
# extractFollowers.grabFollowers(ID)

## Read followers
# listFollowers = readFiles.readJSON()

## Extract Numbers From Twitter
# extractedNumbersTwitter = calculateStats.extractSerialized(listFollowers)

## Prof, Nwalas Follower Count Twitter
# personalCountTwitter = calculateStats.userFriendCountTwitter(extractedNumbersTwitter)

## Calculate mean Twitter
# meanTwitter = calculateStats.calculateMean(extractedNumbersTwitter)

## Calculate median Twitter
# medianTwitter = calculateStats.calculateMedian(extractedNumbersTwitter)

## Calculate standardDev Twitter
# standartDevTwitter = calculateStats.calculateSdv(extractedNumbersTwitter)

## Make Graph Twitter
# createGraph.CumulativeGraph(extractedNumbersTwitter, personalCountTwitter, meanTwitter, medianTwitter, standartDevTwitter)

## Extract Following
# extractFollowers.grabFollowing()

## Read followers
listFollowers = readFiles.readJSON()

## Extract Numbers From Twitter
extractedNumbersTwitterExtraCredit = calculateStats.extractSerialized(listFollowers)

## Prof, Nwalas Friend Count Twitter
personalCountTwitterExtraCredit = calculateStats.userFriendCountTwitter(extractedNumbersTwitter)

## Calculate mean Extra Credit
meanTwitterExtraCredit = calculateStats.calculateMean(extractedNumbersTwitterExtraCredit)

# Calculate median Twitter Extra Credit
medianTwitterExtraCredit = calculateStats.calculateMedian(extractedNumbersTwitterExtraCredit)

## Calculate standardDev Twitter Extra Credit
standartDevTwitterExtraCredit = calculateStats.calculateSdv(extractedNumbersTwitterExtraCredit)

## Make Graph Twitter
createGraph.CumulativeGraph(extractedNumbersTwitterExtraCredit, personalCountTwitterExtraCredit, meanTwitterExtraCredit, medianTwitterExtraCredit, standartDevTwitterExtraCredit)
