# #The Calculator App
# # Objective: The aim of this assignment is to build a basic calculator that can
# # perform addition, subtraction, multiplication, and division.

# #Task 1 - Create functions for each arithmetic operation
   
def basic_calculator ():
   while True:
        print("Welcome to Basic Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit") 
        
# #Task 2 - Use inputs to ask the user what operations they want to perform, 
# # and what numbers they want to use
           
        choice = input("Enter your choice:  ")
        if choice == "5":
            break
        if choice >= "6":
            print("Invalid Choice")
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == "1":
            print(num1 + num2)
        elif choice == "2":
            print(num1 - num2)
        elif choice == "3":
            print(num1 * num2)
        elif choice == "4":

# #Task 3 - Ensure your code can handle division by zero and other potential errors.
# # So if you divide by 0, there is error handling set up to prevent an error 
# # from showing in the console.

            try:
                print(num1 / num2)
            except ZeroDivisionError:
                print("Second number cannot be zero")
        else:
            print("Invalid choice")

basic_calculator()    
        