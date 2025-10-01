# Ib 2nd class Shopping List Manager
shoplist = []

while True:
        print("choice one is to add task. choice 2 is to remove task. choice 3 to show list. choice 4 to exit:")
        choice = input("what is your choice: ")
        
        if choice == "1" :
            task = input("what is your task you want to add:")
            shoplist.append(task)
            print(f"{task} added")
            print(f"shopping list= {shoplist}")
        elif choice == 2: 
            task = input("enter task to remove: ")
        if task in shoplist:
            shoplist.remove(task)
            print(f"'{task} remove")
        else:
            print(f"task not found.")
        if choice == "3":
          if shoplist:
               for i, task in enumerate(shoplist, 1):
                       print(f"{i}. {task}")
        else:
            print("list is empty")
        if choice == "4":
            break