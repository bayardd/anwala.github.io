import matplotlib.pyplot as plt
import numpy as np
import collections

Counter = ({0: 876, 1: 82, 2: 50, 4: 34, 3: 34, 5: 18, 6: 10, 7: 10, 9: 5, 8: 4, 22: 3, 45: 2, 75: 2, 19: 2, 46: 2, 13: 2, 12: 2, 10: 2, 44: 1, 344: 1,43: 1, 39: 1, 11: 1, 48: 1, 25: 1, 47: 1, 991: 1, 31: 1, 16: 1, 21: 1, 406: 1, 17: 1, 85: 1, 451: 1, 321: 1, 116: 1, 27: 1, 29: 1, 257: 1, 125: 1, 23: 1, 156: 1, 14: 1, 212: 1, 60: 1, 32: 1, 147: 1, 109: 1, 18: 1, 69: 1, 4317: 1, 140: 1, 1066: 1, 20: 1, 83: 1, 1765: 1, 180: 1})


xValues = ["0","1","2-4","5-19","20-49","50+"]
yValues = [876, 82,118, 60, 20, 23]


orderedList = collections.OrderedDict(sorted(Counter.items()))


#Used to count amount of each occurancy for yValues
# value = 0
# for i in range(20,50):
# 	if(i in Counter):	
# 		value += Counter[i]
# print(value)





plt.figure(1, figsize=(8, 6))

plt.bar(xValues, yValues)

plt.xlabel("Number of Mementos")
plt.ylabel("Frequency")
plt.title("Histogram Representing Frequency of")
plt.show() 
