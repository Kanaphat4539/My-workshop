import random
import math

myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " ")
#Find summation
mySum = sum(myData)
print("\nSummation = ", mySum)
#Find average
myMean = mySum/len(myData)
print("Average = ", myMean)
#Find maximum
max = max(myData)
print("Maximum = ", max)
#Find minimum
min = min(myData)
print("Minimu = ", min)
#Find variance
myVariance = sum((x-myMean)**2 for x in myData)/len(myData)
print("Variance = ", myVariance)
#Find standard deviation
SD = math.sqrt(myVariance)
print("Standard Deviation = ", SD)