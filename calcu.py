print ("Operations Available are: Addition(1), Subtraction(2), Multiplication(3), or Division(4), all with two numbers: ")
print ("Type in the number next to the operation to select it.")
operation= int(input("Select your operation: "))
if operation == 1:
    print ("Operation selected was addition.")
    num1= int(input("Enter number 1: "))
    num2= int(input("Enter number 2: "))
    print (num1, "+", num2, "=", num1+num2)
elif operation == 2:
    print ("Operation selected was subtraction.")
    num1= int(input("Enter number 1: "))
    num2= int(input("Enter number 2: "))
    print (num1, "-", num2, "=", num1-num2)
elif operation == 3:
    print ("Operation selected was multiplication.")
    num1= int(input("Enter number 1: "))
    num2= int(input("Enter number 2: "))
    print (num1, "x", num2, "=", num1*num2)
elif operation == 4:
    print ("Operation selected was division.")
    num1= int(input("Enter number 1: "))
    num2= int(input("Enter number 2: "))
    print (num1, "/", num2, "=", num1/num2 )
else:
    print ("Invalid operation.")