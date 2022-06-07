symbol = input("what symbol would you like to use? ")
width = int(input("whats the width of your box? "))
height = int(input("whats the height of your box? "))

for x in range(0, height):
    print("")
    for y in range(0, width):
        print(symbol, end="")