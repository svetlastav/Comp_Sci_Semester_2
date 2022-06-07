foodlist = []
total = 0
rangE = int(input("how many items do you want to buy? "))
for i in range(0, rangE):
    item = input("what is the item? ")
    price = int(input("price of item: "))
    foodlist.append(item + " :          $" + str(price))
    total = total + price
print("----------------------------------------------------------")
for x in range(0, rangE):
    print(foodlist[x])
print("----------------------------------------------------------")
print("total:          $" + str(total))
    
    
    



#numitem = int(input("how many items do you want to buy? "))
#total = 0
#for x in range(0, numitem):
 #   item = input("what is the item? ")
  #  price = float(input("price of item: "))
   # total = total + price
#print(total)

