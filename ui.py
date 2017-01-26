import db

while True:
    choice = input("1. Add \n2. Remove \n3. View all \n4. Edit\n5. Quit\n")

    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("That wasn't a valid option, please try again.\n")

    elif choice == "1":
        name = input("Name?\n")
        country = input("Country?\n")
        catches = input("Catches?\n")
        db.add_juggler(name, country, catches)

    elif choice == "2":
        name = input("Name?\n")
        db.remove_juggler(name)

    elif choice == "3":
        db.view_all()

    # Assuming we are updating the highest number of catches
    elif choice == "4":
        name = input("Name?\n")
        catches = input("New high score?\n")
        db.edit(name, catches)

    elif choice == "5":
        break
