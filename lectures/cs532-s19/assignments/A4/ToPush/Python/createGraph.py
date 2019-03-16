import numpy as np
import matplotlib.pyplot as plt
import math

def CumulativeGraph(listFriends, personalCount, mean, median, SDV):

    sorted_data = np.sort(listFriends)
    xValues = []
    yValues = []
    logYValues = []

    for i in range(sorted_data.size):
        # print("x" + str(i))
        # print("y" + str(sorted_data[i]))
        xValues.append(i + 1)

        if(sorted_data[i] >= 1):
            logYValues.append(math.log(sorted_data[i],2))
   
        else:
            logYValues.append(sorted_data[i])

   # Align data with log base 2
    personalCount = round(math.log(int(personalCount), 2))
    mean = round(math.log(mean, 2), 2)
    median = round(math.log(median, 2), 2)
    SDV = round(math.log(SDV, 2), 2)

    #


   # Map X relative to Y
    xNewMean = np.interp(mean, logYValues, xValues)
    xNewPersonal = np.interp(personalCount, logYValues, xValues)
    xNewMedian = np.interp(median, logYValues, xValues)
    xNewSDV = np.interp(SDV, logYValues, xValues)
# interp_func = scipy.interpolate.interp1d(xValues, yValues)
# # Find the intepolated value of y, given x=3.5.
# ynew = interp_func(3.5)
# print ynew

    averageText = "Average: " + str(mean)
    personalText = "Professor Nwalas Friends: " + str(personalCount)
    medianText = "Median: " + str(median)
    standardText = "SD " + str(SDV)

    # print(sorted_data)

    #Cumulative count
    plt.plot(xValues, logYValues)
    plt.plot(xNewMean, mean, markersize=10, marker = ".")
    plt.text(xNewMean, mean-1, averageText, fontsize=9)
    plt.plot(xNewPersonal, personalCount, markersize=10, marker = ".")
    plt.text(xNewPersonal, personalCount+.6, personalText, fontsize=9)
    plt.plot(xNewMedian, median, markersize=8, marker = ".")
    plt.text(xNewMedian, median-1, medianText, fontsize=9)
    plt.plot(xNewSDV, SDV, markersize=10, marker = ".")
    plt.text(xNewSDV-5, SDV+1, standardText, fontsize=9)
    plt.xlabel("Friends")
    plt.ylabel("No. of Friends")
    plt.title("Chart 2 Friends vs FriendCount Twitter Extra Credit  ")
    plt.show()
