# Gestión de inventario
inventory = [
    {"product": "book", "price": 10.0, "quantity": 10},
    {"product": "mouse", "price": 15.0, "quantity": 50},
    {"product": "keyboard", "price": 20.0, "quantity": 30},
    {"product": "monitor", "price": 25.0, "quantity": 10},
    {"product": "headset", "price": 30.0, "quantity": 5}
]

# Validaciones
def confirmation(valor):
    try:
        return 0 < int(valor) < 7
    except ValueError:
        return False

def numint(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def numfloat(valor):
    try:
        
        # Gestión de inventario
inventory = [
    {"product": "book", "price": 10.0, "quantity": 10},
    {"product": "mouse", "price": 15.0, "quantity": 50},
    {"product": "keyboard", "price": 20.0, "quantity": 30},
    {"product": "monitor", "price": 25.0, "quantity": 10},
    {"product": "headset", "price": 30.0, "quantity": 5}
]

# Validación de opción del menú (1-6)
def confirmation(valor):
    try:
        return 1 <= int(valor) <= 6
    except ValueError:
        return False

# Validación de número entero
def numint(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Validación de número decimal
def numfloat(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Pregunta al usuario si desea continuar
def answer():
    while True:
        response = input("Do you want to continue (Yes/No): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Error, please enter 'Yes' or 'No'.")

# Agrega un nuevo producto
def add(product, price, quantity):
    inventory.append({"product": product, "price": float(price), "quantity": int(quantity)})
    print(f"Product '{product}' successfully added.")

# Busca un producto en el inventario
def search(product):
    found = next((item for item in inventory if item["product"] == product), None)
    if not found:
        print("This product is not registered.")
    else:
        print(f"Product: {found['product']} | Price: {found['price']:.2f} | Quantity: {found['quantity']}")

# Actualiza el precio de un producto
def updated_price(product, new_price):
    for item in inventory:
        if item["product"] == product:
            item["price"] = float(new_price)
            print(f"The price of '{product}' has been updated to {new_price:.2f}")
            return
    print("This product is not in inventory.")

# Elimina un producto del inventario
def remove(product):
    global inventory
    new_inventory = [item for item in inventory if item["product"] != product]
    if len(new_inventory) == len(inventory):
        print("This product is not in inventory.")
    else:
        inventory = new_inventory
        print(f"The product '{product}' has been removed from inventory.")

# Calcula el valor total del inventario
def totalvalue():
    if not inventory:
        print("The inventory is empty.")
    else:
        total_value = sum(item["price"] * item["quantity"] for item in inventory)
        print(f"The total value of the inventory is: ${total_value:.2f}")

# Muestra el menú principal
def menu():
    print("\n--- Inventory Management System ---")
    print("1. Add product")
    print("2. Search product")
    print("3. Update price")
    print("4. Remove product")
    print("5. Calculate total inventory value")
    print("6. Exit")

# Ejecuta el sistema
def system():
    while True:
        menu()
        option = input("Select an option (1-6): ").strip()
        if not confirmation(option):
            print("Error: Option must be a number between 1 and 6.")
            continue

        if option == "1":
            while True:
                product = input("Enter product name: ").strip().lower()
                if any(item["product"] == product for item in inventory):
                    print("This product is already registered.")
                    continue
                price = input("Enter the product price: ").strip()
                if not numfloat(price) or float(price) <= 0:
                    print("Error: Price must be a positive number.")
                    continue
                quantity = input("Enter the product quantity: ").strip()
                if not numint(quantity) or int(quantity) <= 0:
                    print("Error: Quantity must be a positive integer.")
                    continue
                add(product, price, quantity)
                if answer() == "no":
                    break

        elif option == "2":
            product = input("Enter product name to search: ").strip().lower()
            search(product)

        elif option == "3":
            product = input("Enter product name to update: ").strip().lower()
            if not any(item["product"] == product for item in inventory):
                print("This product is not registered.")
                continue
            new_price = input("Enter the new price: ").strip()
            if not numfloat(new_price) or float(new_price) <= 0:
                print("Error: Price must be a positive number.")
                continue
            updated_price(product, new_price)

        elif option == "4":
            product = input("Enter product name to remove: ").strip().lower()
            remove(product)

        elif option == "5":
            totalvalue()

        elif option == "6":
            print("
gestion de inventario de la libreria, seguimiento preciso de titulos, cantidad, precios, actualizados, calcular valor total del inventario
inventory = [
    {"product": "book", "price": 10.0, "quantity": 10},
    {"product": "mouse", "price": 15.0, "quantity": 50},
    {"product": "keyboard", "price": 20.0, "quantity": 30},
    {"product": "monitor","price": 25.0, "quantity": 10},
    {"product": "headset", "price": 30.0, "quantity": 5}
]

#creation of functions, and definition of functions

#validation functions and messages
def confirmation(valor):
    try:
        return 0 < float(valor) < 6 
    except ValueError:
        return False
#int validation
def numint(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
#float valitation
def numfloat(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
#menssage validation 
def answer():
     while True:
        answer = input("Do you want to continue(Yes/No): ").strip().lower()
        if answer in ["yes"] or ["no"]:
            return answer
        else:
            print("Error, please enter a correct answer 'Yes' o 'No'.")
#price validation
def pricevalidation(price):
     while True:
         if not (price) or float(price) <= 0:
             print("Error the number must be a positive decimal number.")
         elif numfloat(price) or float(price) >=0:
                 print("price successfully entered and registered")
                 break

#add products function / In this part I create a function that allows us to add the products to our list and dictionary.

def add(product,price,quantity):
    inventory.append({"product":product, "price": price, "quantity" : int(quantity)})
    print(f"product {product}, successfully added.")
        
#search products funtion   /   This function will allow us to search for the product in our list and dictionary with the name and specific information.      
def search(product):
    if product not in inventory:
        print("this product is not registered")
    else:
        price=inventory[product]["price"]
        quantity=inventory[product]["quantity"]
        print(f"product: {product} , price: {price:.2f} | quantity: {quantity}") 
        

# Update the price of an existing product funtion / This function will allow us to change the existing price for a new one.
def updated_price(product, new_price):
    if product not in inventory:
        print("This product is not in inventory")
    else:
        inventory[product]["price"]=new_price
        print(f"The price of the product {product} has been updated to {new_price:.2f}")
        
#function to delete a product / With this function we can search for a product in the list and delete it completely. For this we use the (.pop)
def remove(product):
    if product not in inventory:
        print("This product is not in inventory")
    else:
        inventory.pop(product)
        print(f"The product{product} has been removed from inventory.")
        
        
# funtion to calculate the total value of the inventory / In this function we create a lambda function to add and map the items in the inventory and multiply the price by the quantity of products.
def totalvalue():
    if not inventory:
        print("The inventory is empty.")
    else:
        total_value = sum(map(lambda item: item["precio"] * item["cantidad"], inventory.values()))
        print(f"The total value of the inventory is: ${total_value:.2f}")

# Show main menu / In this part we define the menu as a function to be able to do it in a practical way and to be able to call the menu at any time that is needed with its function.
def menu():
    print("Welcome to the inventory system")
    print("\n Inventory Management System")
    print("1. Add products")
    print("2. Consult product")
    print("3. Update price")
    print("4. Remove products")
    print("5. Calculate total inventory value")
    print("6. Log out")

# Function of executing the system /  In this function we make the steps and the unification of the code, this is where we implement all the functions and give meaning to the code.
def system():
    #here I enter the code in a while loop to create the loop and avoid breaking the code.
    while True:
        menu()
        option = input("Select an option(1-6): ")
        if confirmation(option) == False:
            print("Error, option must be a number between 1 and 6.")
        
            #I add the conditions from the first option and again enter everything in a while loop to avoid code fractures.
        if option == "1":
            while True:
                while True:
                    product=input("Enter the Product Name :").lower()
                    if product not in inventory:
                        print("successfully registered")
                        break
                    else:
                        print(f"This product is already registered,{product}")
                    
                price=input("Enter the value of the product :").strip()
                while True:
                    if not numfloat (price) or float(price) <= 0:
                        print("error the number must be a positive decimal number.")
                        
                    elif numfloat(price) or float(price) >0:
                        print("price entered and recorded successfully")
                        break
                quantity=input("Enter the quantity of products: ").strip()
                while True:
                    if not numint(quantity) or int (quantity) <0:
                        print("Error, the amount must be a positive integer.")
                        
                    elif numint(quantity) or int (quantity) >0:
                        print("Amount entered successfully")
                        break
                add(product,price,quantity)
                print(inventory)
                if answer()== "no" :
                    break
        #I add the second condition and use the search function.
        elif option =="2":
             product=input("Enter the name of the product: ").lower()
             search(product)
            
            #I set the third condition and validate that the data entry is correct, in this case a float type number.
        elif option == "3":
            while True:
                product=input("Enter the name of the product to update: ").lower()
                if product not in inventory:
                    print("This product is not registered in inventory")
                    return
                print(f"Product: {product} | Price: {inventory[product]['price']:.2f} | quantity: {inventory[product]["quantity"]}")
                while True:
                    new_price=float(input("Enter the new price: "))
                    if not numfloat(new_price) or float(new_price) <= 0:
                        print("Error, the price must be a positive decimal number.")
                        return
                    elif numfloat(new_price) or float(new_price) >0:
                        print("price entered and recorded successfully")
                        break
                updated_price(product, new_price)
                if answer()== "yes" :
                    break
              #  I added the 4th condition to remove products, here I used the remove function and a response validation.
        elif option == "4":
            while True:
                product=input("Enter the name of the product to be deleted: ").lower()
                if product not in inventory:
                    print("This product is not in inventory")
                    return
                print(f"The product{product} has been removed from inventory.")
                remove(product) 
                if answer()== "yes" :   
                    break
                # I use the 5th function to calculate the total value, I just call the function
        elif option == "5":
            totalvalue()
            
            #In this last option, the rest closes the code and thus can break the complete cycle of this, and close the system.
        elif option == "6":
            print("Leaving the program. See you soon!")
            break
        else:
            print("Error, Invalid option. Please try again.")
    
system()
            
                
