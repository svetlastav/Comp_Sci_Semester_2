people_list = ["Kanye", "your grandmother", "Pete Davidson", "your mom", "claire", "mr. poole", "shauna"]
compliment_list = [" is cool", " is smart", " is a girlboss", " is looking spicy", " is kind", " has a fatty"]

import random
num_people = random.randrange(0, len(people_list))
num_compliment = random.randrange(0, len(compliment_list))

print(people_list[num_people] + compliment_list[num_compliment])