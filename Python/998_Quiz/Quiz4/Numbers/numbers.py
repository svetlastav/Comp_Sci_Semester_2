mynumbers = [6, 9, 32, 28, 15, 22, 3, 18]
max = mynumbers[0]
min = mynumbers[0]
length = len(mynumbers)
for i in range(0, length):
    if (mynumbers[i] > max):
        max = mynumbers[i]
for i in range(0, length):
    if (mynumbers[i] < min):
        min = mynumbers[i]
sum = 0
for i in range(0, length):
    sum = sum + mynumbers[i]
average = sum/length
print("the max is: " + str(max))
print("the min is : " + str(min))
print("the average is : " + str(average))