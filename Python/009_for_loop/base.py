length = int(input("please enter a line length: "))
rawr = input("do you want a verticle or horizontal line: ")
pew = "_"
for x in range(0, length):
    if(rawr == "horizontal"):
        print(pew, end="")
    elif(rawr == "verticle"):
        print(pew)