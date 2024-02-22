    print("Options");
    print("1. Add item to the shopping list")
    print("2. View shopping list");
    print("3. Remove item from the shopping list");
    print("4. Quit")

    shopping_list = [];

    chosen_number = int(input("\nEnter the number of your choice: "));
    while chosen_number != 4:

    if (chosen_number == 1):
            new = input("Enter the item you want to add: ");
            new_item = new.lower()
            
            shopping_list.append(new_item);
            print(f"{new_item} has been added to your shopping list")

    elif chosen_number == 2:
            for i in range(len(shopping_list)):
                print(i + 1, "-", shopping_list[i]);


    elif chosen_number == 3:
            remove = input("Enter the item you want to remove: ");
            remove_item = remove.lower();

            for i in range(len(shopping_list)):
                if shopping_list[i] == remove_item:
                    shopping_list.remove(shopping_list[i])
            print(f"{remove_item} has been removed to your shopping list")

    print("\nOptions");
    print("1. Add item to the shopping list")
    print("2. View shopping list");
    print("3. Remove item from the shopping list");
    print("4. Quit")

    chosen_number = int(input("\nEnter the number of your choice: "));

    if chosen_number == 4:
        print("Goodbye!")