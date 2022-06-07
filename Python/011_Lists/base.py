one = "When life gives you melons, you might be dyslexic"
two = "Blunt pencils are really pointless"
three = "I got kicked out of a secret cooking society, I spilled the beans"
four = "The rotation of earth really makes my day"
five = "Pollen is what happens when they cant keep it in their plants"
jokes = [one, two, three, four, five]

import random
num = random.randrange(0,5)
if num == 0:
    print(jokes[0])
if num == 1:
    print(jokes[1])
if num == 2:
    print(jokes[2])
if num == 3:
    print(jokes[3])
if num == 4:
    print(jokes[4])
    