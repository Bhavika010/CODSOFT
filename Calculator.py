print("Mini Calulator")
print(("1. Addition \n2. Subtraction  \n3. Multiplication \n4. Division"))
choice = int(input("Enter your choice: "))
num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))
if choice ==1:
    print("The Addition of the given number is ", num1 + num2)
elif choice ==2:
    print("The Subtraction of the given number is ", num1 - num2)
elif choice ==3:
    print("The Multiplication of the given number is ", num1 * num2)
elif choice ==4:
    print("The Division of the given number is ", num1 / num2)
    
