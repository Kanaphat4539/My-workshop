import random

myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " ")
#Find summation
sum = sum(myData)
print("\nSummation = ", sum)
#Find average
avg = sum/len(myData)
print("Average = ", avg)
#Find maximum
max = max(myData)
print("Maximum = ", max)
#Find minimum
min = min(myData)
print("Minimu = ", min)
