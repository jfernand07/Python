#gestion de inventario de la libreria, seguimiento preciso de titulos, cantidad, precios, actualizados, calcular valor total del inventario

inventory = [
    {"title": "100 años de soledad", "price": 10.0, "quantity": 10},
    {"title": "La Va llena", "price": 15.0, "quantity": 50},
    {"title": "superacion personal", "price": 20.0, "quantity": 30},
    {"title": "spiderman","price": 25.0, "quantity": 10},
    {"title": "La culpa es de la vaca", "price": 30.0, "quantity": 5}
]


#funtions
# option validation
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
        answer = input("Would you like to continue? (Yes/No): ").strip().lower()
        if answer in ["Yes"] or ['no']:
            return answer 
        else:
            print("Invalid answer. Please enter 'yes' or 'no'.")
#price validation
def pricevalidation(price):
     while True:
         if not (price) or float(price) <= 0:
             print("Error the number must be a positive decimal number.")
         elif numfloat(price) or float(price) >=0:
                 print("price successfully entered and registered")
                 break
#add book 
def add(title,price,quantity):
    inventory.append({"name":title, "price": float(price), "quantity" : int(quantity)})
    print(f"Book {title}, successfully added.")
        
#search books
def search(title):
    if title not in inventory:
        print("this book is not registered")
    else:
        price=inventory[title]["price"]
        quantity=inventory[title]["quantity"]
        print(f"Book: {title} | price: {price:.2f} | quantity: {quantity}")   

#update price
def updateprice(title, newprice,newquantity):
    if title not in inventory:
        print("This product is not in stock")
    else:
        inventory[title]["price"]=newprice
        inventory[title]["quantity"]=newquantity
        print(f"The price of the book {title} was change to {newprice:.2f} and the quantity is {newquantity}")
    
#remove books
def Removebook(title):
    if title not in inventory:
        print("this book is not registered in the inventory")
    else:
        inventory.pop(title)
        print(f"the book was removed {title}of the inventory")
        
#total value in inventory 
def totalvalue():
    if not inventory:
        print("Inventory is empty.")
    else:
        totalvalue = sum(map(lambda item: item["price"] * item["quantity"], inventory.values()))
        print(f"The total value of the inventory is: ${totalvalue:.2f}")
        
#menu
def menu():
    print("Welcome to inventory System")
    print("select the desired option")
    print("1. Add Books")
    print("2.Search Books")
    print("3.Update Price")
    print("4. Remove Books in inventory")
    print("5.Total value in inventory")
    print("6.Sign out")

    
#Run System
def system():
    while True:
        menu()
        option=input("Please write the number of the action you wish to perform").title()
        if confirmation(option)== False:
            print("Error, you must enter a number between 1 to 6")
        if option=="1":
            while True:
                while True:
                    title= input("Please enter the name of the book you want to add").title()
                    if title not in inventory:
                        print("The registration was correct")
                        break
                    else:
                        print(f"This book is already registered in the inventory",title)
                price= float(input("Please enter the price of the book"))
                while True:
                    if not numfloat (price) or float(price) <= 0:
                        print("Error el numero debe de ser un numero decimal positivo.")
                            
                    elif numfloat(price) or float(price) >=0:
                        print("Precio ingresado y registrado con exito")
                        break
                quantity=int(input("Please enter the quantity of books"))
                while True:
                    if not numint(quantity) or int(quantity)<=0:
                        print("Error, Enter a valid amount")
                            
                    elif numint(quantity) or int(quantity) >0:
                        print("Amount successfully entered and registered")
                    add(title,price,quantity)
                    print(inventory)
                    if answer()== "No":
                        break
        elif option =="2":
             title=input("Enter the name of the book").title()
             search(title)
        elif option=="3":
            while True:
                title=input("Enter the name of the book you wish to change the price of") 
                if title not in inventory:
                   print("This product is not in stock")  
                   return  
                newprice=float(input("Ingrese el nuevo precio: "))
                while True:
                    if not numint(newprice) or float(newprice) <= 0:
                        print("Error, the price must be a positive decimal number..")
                        return
                    elif numfloat(newprice) or float(newprice) >=0:
                        print("price successfully entered and registered")
                        break
                updateprice(title, newprice)
                if answer()== "Yes" :
                    break
        elif option=="4":
            while True:
                title=input("Enter the name of the Book to delete: ").lower()
                if title not in inventory:
                    print("This product is not in stock")
                    return
                print(f"The Book{title} was removed.")
                Removebook(title) 
                if answer()== "Yes" :   
                    break
                
        elif option=="5":
            totalvalue()
        elif option=="6":
            print("Leaving the program. See you soon!")
            break
        else:
            print("Invalid option. Try again.")
system()
            
                