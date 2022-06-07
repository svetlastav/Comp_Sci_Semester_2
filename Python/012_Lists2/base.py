import random
cow = [0,1,2,3,4,5,6,7,8,9]
joe = int(input("How many random numbers would you like? "))
for i in range(0, joe - 1):
    rawr = random.randrange(9)
    print(cow[rawr], end=", ")
print(cow[random.randrange(9)])
