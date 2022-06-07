import random
restlist = ["sushi stop", "olive garden", "chipotle", "wingstop"]
sushistop = ["hand rolls", "tempura rolls", "nigiri", "miso soup", "edamame"]
oliveGar = ["spaghetti", "fettucini alfredo ", "ceaser salad", "breadsticks"]
chipOtle = ["burrito", "bowl", "quesedillas", "tacos"]
wingstOp = ["fries", "lemonon pepper wings", "barbeque wings", "spicy wings", "rainbow wings"]

choice = input("pick a restaurant : sushi stop, olive garden, chipotle, wingstop ")
if(choice == "sushi stop"):
   for i in range(0, len(sushistop)):
       print(sushistop[i])
       suggs = random.randrange(0, len(sushistop))
   print("reccomended item : " + sushistop[suggs])
elif(choice == "olive garden"):
    for i in range(0, len(oliveGar)):
        print(oliveGar[i])
        suggo = random.randrange(0, len(oliveGar))
    print("reccomended item : " + oliveGar[suggo])
elif(choice == "chipotle"):
    for i in range(0, len(chipOtle)):
        print(chipOtle[i])
        suggc = random.randrange(0, len(chipOtle))
    print("reccomended item : " + chipOtle[suggc])
elif(choice == "wingstop"):
    for i in range(0, len(wingstOp)):
       print(wingstOp[i])
       suggw = random.randrange(0, len(wingstOp))
    print("reccomended item : " + wingstOp[suggw])