#The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users 
# make a shopping list.

#Task ! - Write a function that lets the user add items to a list
           
products = []

def shopping_list():
    while True:
        print("\n Shopping List Maker")
        print("1. View Shopping List")
        print("2. Add Items")
        print("3. Remove Items")
        print("4. Print Shopping List")
        print("5. Exit")
        choice = input("Enter your choice:  ")
        
        if choice == "1":
            print("\n Current Shopping List")
            for product in products [:100]:
                print(product)
            if len(products) > 100:
                print("...and more")           
        elif choice == "2":
            new_product = input("Enter the new item:  ").upper()
            products.append(new_product)
            print(f"{new_product} has been added to the shopping list")
            
#Task 2 - Include a function to remove items from the list       

        elif choice == "3":
            product_to_remove = input("Enter the name of the item to remove \n").upper()
            if product_to_remove in products:
                products.remove(product_to_remove)
                print(f"{product_to_remove} has been removed from the shopping list")
            else:
                print(f"{product_to_remove} has not found in the shopping list.")
                
                
 #Task 3 Add a function that prints out the entire list in a formatted way               
        elif choice =="4":
            print(f"Here is your current shopping list {products}")
        elif choice == "5":
            print("Exiting the shopping list")

shopping_list()




