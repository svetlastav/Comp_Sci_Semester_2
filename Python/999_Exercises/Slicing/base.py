name = input("Please enter a first and last name : ")
y = 0
s = 1
for i in range (0, len(name)):
    letter = name[y : s]
    print(letter)
    y = y + 1
    s = s + 1
    if ((name[y : s]) == " "):
       start = y
       end = s
       
print(name[start+1: len(name)] + " ", end="")
print(name[0 : start])
    #print(name[y: len(name)])