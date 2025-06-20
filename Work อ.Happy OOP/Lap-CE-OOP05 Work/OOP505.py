import random
import statistics

class theData:
    def __init__(self, myData):
        self._myData = myData
    def Display(self):
        print(self._myData)
class theSummation(theData): 
    def mySummation(self):
        self._mySum = sum(self._myData); print("Summation = ", self._mySum)
class theMean(theData):
    def myMean(self):
        self._Mean = sum(self._myData)/len(self._myData); print("Mean = ", self._Mean)
class theMax(theData):
    def Maximum(self):
        self._myMax = max(self._myData); print("Maximum = ", self._myMax)
class theMin(theData):
    def Minimum(self):
        self._myMin = min(self._myData); print("Minimun = ", self._myMin)
class theVariance(theData):
    def myVariance(self):
        self._myVar = statistics.variance(self._myData); print("Variance = ", self._myVar)
class theSD(theData):
    def mySD(self):
        self._SD = statistics.stdev(self._myData); print("Standard Deviation = ", self._SD)
class theSorted(theData):
    def mySorted(self):
        self._mySorted = sorted(myData); print("Sorted number = ", self._mySorted)
class theMedian(theData):
    def myMedian(self):
        self._myMedian = statistics.median(myData); print("Median = ", self._myMedian)

myData = [90,40,84,31,44,20,97,56,45,16,41,83]
I_need_to_know = theData(myData); I_need_to_know.Display()
I_need_to_know = theSummation(myData); I_need_to_know.mySummation()
I_need_to_know = theMean(myData); I_need_to_know.myMean()
I_need_to_know = theMax(myData); I_need_to_know.Maximum()
I_need_to_know = theMin(myData); I_need_to_know.Minimum()
I_need_to_know = theVariance(myData); I_need_to_know.myVariance()
I_need_to_know = theSD(myData); I_need_to_know.mySD()
I_need_to_know = theSorted(myData); I_need_to_know.mySorted()
I_need_to_know = theMedian(myData); I_need_to_know.myMedian()