first = int(input("enter a number: "))
operation = input("enter an operation: ")
second = int(input("enter a second number: "))

if(operation == "+"):
    ans = str(first+second)
elif(operation == "-"):
    ans = str(first-second)
elif(operation == "/"):
    ans = str(first/second)
elif(operation == "*"):
    ans = str(first*second)

print(str(first) + operation + str(second) + "=" + ans)