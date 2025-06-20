import random

myData = [random.randint(1,100) for i in range(20)]
print(myData, end = " ")

sum = 0
for i in myData:
    sum = sum+i
print("\nSummation = ", sum)
avg = sum/len(myData)
print("Average = ",avg)
max = myData[0]; min = myData[0]
for i in myData:
    if max < i:
        max = i
    else:
        max = max
print("Maximum = ",max)
for i in myData:
    if min > i:
        min = i
    else:
        min = min
print("Minimum = ",min)
