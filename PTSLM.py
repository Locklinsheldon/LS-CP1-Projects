#Locklin Sheldon, SkillPractice: Shopping List Manager
shoppingList = []


def add():
    item = input("Insert item: ")
    shoppingList.append(item)
    print("Item added.")
    print("Current shopping list:", shoppingList)


def remove():
    item = input("Enter item to remove: ")
    if item in shoppingList:
        shoppingList.remove(item)
        print("Item removed.")
    else:
        print("Item not found.")
    print("Current shopping list:", shoppingList)


while True:
    action = input("""What would you like to do?
                    Enter 1 to add item
                    Enter 2 to remove item
                    Enter 3 to leave the list:\n""")


    if action == "1":
        add()
    elif action == "2":
        remove()
    else:
        print("Have a nice day:)")
       

