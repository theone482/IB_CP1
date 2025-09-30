# Ib 2nd class Shopping List Manager
shoplist = []

while True:
        print("choice one is to add task. choice 2 is to remove task. choice 3 to show list. choice 4 to exit:")
        choice = input("what is your choice: ")
        
        if choice == "1" :
            action = input("what is your task you want to add:")
            shoplist.append(action)
            print(f"{action} added")
            print(f"shopping list= {shoplist}")
        elif choice == 2: 
            action = input("enter task to remove: ")
            if action in shoplist:
                 shoplist.remove(action)
                 print(f"'{action} remove")
            else:
                 print(f"task not found.")
        elif choice == "3":
             if shoplist:
                  for i, action in enumerate(shoplist, 1):
                       print(f"{i}. {action}")
        else:
             print("list is empty")
        if choice == "4":
            break