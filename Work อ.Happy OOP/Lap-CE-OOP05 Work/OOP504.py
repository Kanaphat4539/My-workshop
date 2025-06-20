import random
import statistics

class myStat:
    def __init__(self, myData):
        self.myData = myData
    def mySummation(self):
        self.mySum = sum(self.myData); print("Summation = ", self.mySum)
    def myMean(self):
        self.Mean = sum(myData)/len(myData); print("Mean = ", self.Mean)
    def myMaximum(self):
        self.myMax = max(myData); print("Maximum = ", self.myMax)
    def myMinimum(self):
        self.myMin = min(myData); print("Minimu = ", self.myMin)
    def myVariance(self):
        myVar = statistics.variance(self.myData); print("Variance = ", myVar)
    def mySD(self):
        SD = statistics.stdev(self.myData);print("Standard Deviation = ", SD)

myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " "); print()
I_need_to_know = myStat(myData)
I_need_to_know.myMean()
I_need_to_know.myMaximum(); I_need_to_know.myMinimum()
I_need_to_know.myVariance(); I_need_to_know.mySD()